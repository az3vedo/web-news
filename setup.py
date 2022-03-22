import os

# set FLASK_APP=app
# set FLASK_ENV=%1

os.environ['FLASK_APP']=app
os.environ['FLASK_ENV']=sys.argv[1] | "production"
os.system('pip install - r ./requirements.txt')
# if (os.name == "nt"):
    
# elif (os.name == "unix"):

# else:
#     print("Erro: Sistema Operacional inválido")