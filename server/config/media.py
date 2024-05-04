import os

from server.config.settings import get_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_DIR = os.path.join(BASE_DIR, 'media')
os.path.exists(MEDIA_DIR) or os.makedirs(MEDIA_DIR)
MEDIA_URL = get_settings().api_domain + '/media/'
