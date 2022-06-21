import os
import sys

try:
    env = sys.argv[1]
except:
    env = "production"

os.environ['FLASK_APP']="app"
os.environ['FLASK_ENV']=env
os.system('pip install -r ./requirements.txt')
os.system('gunicorn app:app -b 127.0.0.1:5001')
