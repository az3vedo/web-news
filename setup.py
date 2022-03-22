import os
import sys

try:
    env = sys.argv[1]
except:
    env = "production"

os.environ['FLASK_APP']="app"
os.environ['FLASK_ENV']=env
os.system('pip install -r ./requirements.txt')
os.system('flask run --port 5001')
