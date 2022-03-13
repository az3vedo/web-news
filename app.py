from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape


app = Flask(__name__)
noticias = [
            {
              "titulo": "Acidente de carro",
              "autor": "Pedro Cabral",
              "categoria": "sensacionalismo",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Ganhador da loteria",
              "autor": "João das Neves",
              "categoria": "falta do que fazer",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            }
          ]
env = Environment(
  loader=PackageLoader("app"),
  autoescape=select_autoescape()
)

@app.route("/")
def home():
  template = env.get_template("index.html")
  return render_template(template, noticias=noticias, page={"title":"Web News"})

@app.route("/categorias")
def category():
  template = env.get_template("categorias.html")
  return render_template(template, page={"title":"Categorias"})

