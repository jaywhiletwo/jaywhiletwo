from django.core.management import BaseCommand, CommandError
from django.conf import settings
import subprocess

from photo.models import Gallery


class Command(BaseCommand):
    def handle(self, *args, **options):
        extensions = ['jpg', 'png', ]
        HELP_MSG = 'Usage: ./manage.py generate_tns <dir_name>\nAccepts extensions: %s' % extensions
        if len(args) != 1:
            raise CommandError(HELP_MSG)

        dir_name = args[0]
        g = Gallery.objects.filter(dir_name=dir_name).first()
        if not g:
            raise CommandError('Gallery with dir_name %s does not exist.' % dir_name)

        full_dir_name = settings.LOCAL_RESOURCE + dir_name
        try:
            self.stdout.write('Processing %s\n' % full_dir_name)
            files = subprocess.check_output(['ls', '%s' % full_dir_name]).split('\n')
            tn_dir = '%s/tn' % full_dir_name
            print tn_dir
            subprocess.check_output(['mkdir', '-p', tn_dir]).split('\n')
            self.stdout.write('Found %s files\n' % len(files))
        except subprocess.CalledProcessError:
            raise CommandError('Directory "%s" does not exist' % full_dir_name)
        else:
            for file in files:
                filename, ext = '.'.join(file.split('.')[:-1]), file.split('.')[-1]
                if ext.lower() in extensions:
                    full_file = '%s/%s' % (full_dir_name, file)
                    tn_file = '%s/tn/%s' % (full_dir_name, file)
                    print full_file, tn_file
                    subprocess.check_output(['convert', '-thumbnail', '200', full_file, tn_file])
