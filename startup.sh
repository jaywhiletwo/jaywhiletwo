#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

./manage.py collectstatic --noinput
bower install masonry