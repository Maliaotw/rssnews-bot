import os
import environ

# BASE
# ------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR, 'files')
ACCESSKEY_FILE = os.path.join(FILES_DIR, 'acesskey.json')

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(env_file):
    # Use a local secret file, if provided
    env.read_env(env_file)

# API
# ------------------------------------------------------------------------------
API_URL = env.str('API_URL')
API_KEYWORD = env.str('API_KEYWORD')
# API_ID = os.environ.get('API_ID')
# API_SECRET = os.environ.get('API_SECRET')

# TELEGRAM
# ------------------------------------------------------------------------------
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = env.str("TELEGRAM_CHANNEL_ID")
TELEGRAM_CHANNEL_ERROR_ID = env.str("TELEGRAM_CHANNEL_ERROR_ID")
TELEGRAM_OWNER_ID = env.str("TELEGRAM_OWNER_ID")

# WEB Server
# ------------------------------------------------------------------------------
BOOTSTRAP_TOKEN = env.str('BOOTSTRAP_TOKEN')

DEBUG = env.bool('DEBUG', False)

if DEBUG:
    # import secrets
    # BOOTSTRAP_NAME = secrets.token_hex(6)
    BOOTSTRAP_NAME = "7c8723f58f9g"
    API_URL = "http://127.0.0.1:8000"
else:
    import socket

    BOOTSTRAP_NAME = socket.gethostname()[:32]
