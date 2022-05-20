# web-news
Portal de notícias

### Integrantes
 - Gabriel Azevedo de Souza
 - Maria Eduarda Basílio de Oliveira

### Instruções para executar o projeto

#### Primeiros passos
- Necessário python3.6 ou superior;
- Criar uma virtualenv 
 ```bash
 # Caso tenha o python no path
  venv env
 # Caso não tenha
  python -m venv env
 ```
 - Iniciar a virtualenv
  ```bash
 # Linux
   source env/bin/activate
 # Windows
   cd env/Scripts/
   activate.bat
 ```
 - Instalar as bibliotecas
  ```bash
    pip install -r requirements.txt
  ```
 - Execução do projeto
  ```bash
  python setup.py
   
  # o setup iniciara o projeto com o ambiente de produção, para utilizar o ambiente de dev adicione o argumento "development": 
   python setup.py development
 ```
