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