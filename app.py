from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from services.api import Api

app = Flask(__name__)
noticias = [
            {
              "titulo": "Time da cidade passa para as semi-finais!",
              "autor": "Pedro Cabral",
              "categoria": "Esporte",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Vai chover canivetes!",
              "autor": "João das Neves",
              "categoria": "Clima e previsão do tempo",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            },
            {
              "titulo": "Novo esporte domina as escolas da cidade",
              "autor": "João das Neves",
              "categoria": "Esporte",
              "materia": "Pedro Paulo Ricardo Gabriel Maria Fabricio Fernando José Raul William Douglas Charles Beatriz Vitória Bianca"
            }
          ]
categorias = "EsportevwsOportunidade e empregovwsClima e previsão do tempovwsCiência e Tecnologia".split('vws')

def select_article_category(category):
  result = list(filter(lambda x: x["categoria"] == category, noticias))
  return result


env = Environment(
  loader=PackageLoader("app"),
  autoescape=select_autoescape()
)

@app.route("/")
def home():
  noticias = Api.getNoticias()
  template = env.get_template("index.html")
  return render_template(template, noticias=noticias, page={"title":"Web News"})

@app.route("/categorias")
def category():
  categorias = Api.getAssuntos()
  template = env.get_template("categorias.html")
  return render_template(template,categorias=categorias, page={"title":"Categorias"})

@app.route("/noticias_categorias/<id>")
def show_noticias_by_categorias(id):
  noticias = Api.getNoticiasByAssunto(id)
  template = env.get_template("index.html")
  return render_template(template,noticias=noticias, page={"title":"Notícias"})

if __name__ == '__main__':
  app.run()