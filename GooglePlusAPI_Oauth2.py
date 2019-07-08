# Getting own account details of Google Plus
from google_auth_oauthlib.flow import Flow
import os
import json
from googleapiclient.discovery import build
import hashlib
import pymongo
flow = Flow.from_client_secrets_file(
    r'C:\Users\SOUMITA\PycharmProjects\WebScience_Crawler\client_secret.json',
    scopes=['https://www.googleapis.com/auth/plus.me'],
    redirect_uri='https://www.blogger.com')
auth_url, _ = flow.authorization_url(prompt='consent')
print('Please go to this URL: {}'.format(auth_url))
code = input('Enter the authorization code:')
flow.fetch_token(code=code)
print(code)
session = flow.authorized_session()
v=session.get('https://www.googleapis.com/plus/v1/people/me').json()
print(v)