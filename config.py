""""
MIT License

Copyright (c) 2022 Timothy Rezendes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
	NYT_KEY = os.environ.get('NYT_KEY')
	WORDNIK_KEY = os.environ.get('WORDNIK_KEY')
