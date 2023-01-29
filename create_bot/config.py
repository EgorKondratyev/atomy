import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
admins = list(map(int, os.getenv('ADMIN').split(',')))
