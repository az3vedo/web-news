from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from waitress import serve

# Informações de execução, não alterar
PORT=5001
app = Flask(__name__)
if(__name__=='__main__'):
  serve(app, host='0.0.0.0', port=PORT)

# Mock de dados, apagar assim que o banco de dados for implementado
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
  template = env.get_template("index.html")
  return render_template(template, noticias=noticias, page={"title":"Web News"})

@app.route("/categorias")
def category():
  template = env.get_template("categorias.html")
  return render_template(template,categorias=categorias, page={"title":"Categorias"})

@app.route("/categorias/<categoria>")
def show_category(categoria):
  template = env.get_template("index.html")
  return render_template(template,noticias=select_article_category(categoria), page={"title":"Notícias"})
