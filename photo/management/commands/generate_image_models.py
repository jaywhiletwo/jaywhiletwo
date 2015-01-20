from django.core.management import BaseCommand, CommandError
from django.conf import settings
import subprocess

from photo.models import Image, Gallery


class Command(BaseCommand):
    def handle(self, *args, **options):
        extensions = ['jpg', 'png', ]
        HELP_MSG = 'Usage: ./manage.py generate_image_models <dir_name>\nAccepts extensions: %s' % extensions
        if len(args) != 1:
            raise CommandError(HELP_MSG)

        dir_name = args[0]
        g = Gallery.objects.filter(dir_name=dir_name).first()
        if not g:
            self.stdout.write('Gallery with dir_name %s does not exist. Create it? (y/n)' % dir_name)
            if raw_input().lower() != 'y':
                return
            else:
                g = Gallery(dir_name=dir_name, display_name=dir_name, summary='New gallery')
                g.save()

        full_dir_name = settings.LOCAL_RESOURCE + dir_name
        try:
            self.stdout.write('Processing %s\n' % full_dir_name)
            files = subprocess.check_output(['ls', '%s' % full_dir_name]).split('\n')
            self.stdout.write('Found %s files\n' % len(files))
        except subprocess.CalledProcessError:
            raise CommandError('Directory "%s" does not exist' % full_dir_name)
        else:
            for file in files:
                filename, ext = '.'.join(file.split('.')[:-1]), file.split('.')[-1]
                if ext.lower() in extensions:
                    if Image.objects.filter(filename=filename).filter(extension=ext).filter(gallery=g).exists():
                        self.stdout.write('Skipping file: %s\n' % file)
                    else:
                        image = Image.objects.create(gallery=g)
                        image.filename = filename
                        image.extension = ext
                        self.stdout.write('Processed file: %s\n' % image.filename)
                        image.save()
