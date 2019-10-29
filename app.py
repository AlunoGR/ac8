from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return rendertemplates("index.html")

@app.route('/lista.html')
def ListadeCursos():
    return rendertemplates("lista.html")

@app.route('/detalhes.html')
def DetalhedeCurso():
    return rendertemplates("detalhes.html")

@app.route('/disciplina.html')
def Disciplina():
    return rendertemplates("disciplina.html")

@app.route('/noticias.html')
def Notícias():
    return rendertemplates("noticia.html")


app.run()
