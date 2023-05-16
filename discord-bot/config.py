import os
from dotenv import load_dotenv

# load values from .env file
load_dotenv()

# define configuration variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
GRAFANA_URL = os.getenv('GRAFANA_URL')
GRAFANA_API_KEY = os.getenv('GRAFANA_API_KEY')
REPLIT_API_KEY = os.getenv('REPLIT_API_KEY')

# Google Docs API keys
GOOGLE_DOCS_CLIENT_ID = os.getenv('GOOGLE_DOCS_CLIENT_ID')
GOOGLE_DOCS_CLIENT_SECRET = os.getenv('GOOGLE_DOCS_CLIENT_SECRET')
GOOGLE_DOCS_REFRESH_TOKEN = os.getenv('GOOGLE_DOCS_REFRESH_TOKEN')
