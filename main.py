from flask import Flask, render_template
#Como o Flask é um framework ele exige algumas regras e nomes q sempre tem ser usado, diferente das bibliotecas
#olha no site do Flask pra saber das regras(ex:a pasta criada tem q ter nome de "templates")

app = Flask(__name__)

#route -> josiasbroch.com/contatos ->Esse "contatos" seria o "route"
#função -> o que você quer exibir naquela página
#template

@app.route("/") #app = pq la em cima dei o nome do site de app, route = definir o link da pagina
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos(): #<p> = começar paragrafo em html, </p> = terminar paragrafo em html
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")#colocar o nome do usuario q esta no link do site para a tela de navegar. faz todos esses passos
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
