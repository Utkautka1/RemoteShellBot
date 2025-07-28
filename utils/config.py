import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:3000/api')

# Роли пользователей
ROLE_USER = 'user'
ROLE_ADMIN = 'admin' 