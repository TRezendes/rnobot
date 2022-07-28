import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv('.env')

class Config(object):
	API_KEY = os.environ.get('API_KEY')
	API_SECRET = os.environ.get('API_SECRET')
	BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
	ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
	ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
	OAUTH2_ID = os.environ.get('OAUTH2_ID')
	OAUTH2_SECRET = os.environ.get('OAUTH2_SECRET')
