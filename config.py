import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv('.env')

class Config(object):
	API_KEY = os.environ.get('API_KEY')
	API_SECRET = os.environ.get('API_SECRET')
	BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
