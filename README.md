# Wagtail-Blog
My personal portfolio website, ported to use wagtail

## Getting started
after cloning the repo, naviate into the folder and run
'''
./manage.py makemigrations && ./manage.py migrate
'''
As this repo is connected to CI you may want to change settings.py from settings.production to settings.dev for easier debugging.

Then run

'''
./manage.py collectstatic
'''

Finally

'''
./manage.py runserver
'''
