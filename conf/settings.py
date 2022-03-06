import os

# BASE
# ------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR, 'files')
ACCESSKEY_FILE = os.path.join(FILES_DIR, 'acesskey.json')

# API
# ------------------------------------------------------------------------------
API_URL = os.environ.get('API_URL')
API_KEYWORD = os.environ.get('API_KEYWORD')
# API_ID = os.environ.get('API_ID')
# API_SECRET = os.environ.get('API_SECRET')

# TELEGRAM
# ------------------------------------------------------------------------------
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID")
TELEGRAM_CHANNEL_ERROR_ID = os.environ.get("TELEGRAM_CHANNEL_ERROR_ID")
TELEGRAM_OWNER_ID = os.environ.get("TELEGRAM_OWNER_ID")

# WEB Server
# ------------------------------------------------------------------------------
BOOTSTRAP_TOKEN = os.environ.get('BOOTSTRAP_TOKEN')

DEBUG = os.environ.get('DEBUG')

if DEBUG:
    # import secrets
    # BOOTSTRAP_NAME = secrets.token_hex(6)
    BOOTSTRAP_NAME = "7c8723f58f9g"
    API_URL = "http://127.0.0.1:8000"
else:
    import socket

    BOOTSTRAP_NAME = socket.gethostname()[:32]
