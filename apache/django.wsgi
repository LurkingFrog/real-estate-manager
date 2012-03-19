import os, sys

prev_sys_path = list(sys.path)

sys.path.append('/var/www/real_estate/')
sys.path.append('/var/www/real_estate/apps')
sys.path.append('/var/www/real_estate/apps/main')

import site
site.addsitedir('/home/dfogelson/pyenv/py27/lib/python2.7/site-packages/')

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()