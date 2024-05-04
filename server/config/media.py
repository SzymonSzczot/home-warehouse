import os

from server.config.settings import get_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_URL = get_settings().api_domain + '/media/'
