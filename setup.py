import os
import sys

try:
    env = sys.argv[1]
except:
    env = "production"

os.system('pip install -r ./requirements.txt')
os.system('flask run')
