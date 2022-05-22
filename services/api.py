import requests, json

host = 'http://localhost:5101/api'

class Api:
  
  def getNoticias():
    url = f"{host}/noticias/"
    data = requests.get(url)
    return(data.json())

  def getNoticiaById(id):
    url = f"{host}/noticias/{id}"
    data = requests.get(url)
    return(data.json())

  def getAssuntos():
    url = f"{host}/assuntos/"
    data = requests.get(url)
    return(data.json())
  
  def getNoticiasByAssunto(id):
    url = f"{host}/noticias/assuntos/{id}"
    data = requests.get(url)
    print(data)
    return(data.json())