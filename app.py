from email.mime import application
from flask import Flask, Response, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///compras.db'

db = SQLAlchemy(app)

class Listas_compras(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    nome = db.Column(db.String(50), nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
    valor = db.Column(db.Numeric(10,2),  nullable = False)

    def to_json(self):
        return{"id":self.id, "nome":self.nome,"quantidade":self.quantidade,"valor":self.valor}
    
db.create_all()

#Home
@app.route("/")
def home():
    return render_template('home.html')

#Lista
@app.route("/listando")
def listando():
    return render_template('lista.html')

#selecionar tudo
@app.route("/lista", methods=["GET"])
def seleciona_compras():
    listas_classes = Listas_compras.query.all()
    listas_json = [lista.to_json() for lista in listas_classes]

    return json.dumps(listas_json)


#Selecionar Individual
@app.route("/lista/<id>", methods=["GET"])
def seleciona_compra(id):
    lista_classe = Listas_compras.query.filter_by(id=id).first()
    lista_json = lista_classe.to_json()

    return gera_response(200, "Lista",lista_json)
#Cadastrar
@app.route("/lista", methods=["POST"])
def criar_dado():
    body = request.get_json()
    #validar os parametros
    try:
        lista = Listas_compras(nome=body["nome"], quantidade=body["quantidade"], valor=body["valor"])
        db.session.add(lista)
        db.session.commit()
        return gera_response(201,"lista", lista.to_json(), "Criado com Sucesso")
    except Exception as e:
        print('Erro',e)
        return gera_response(400,"lista", {}, "Erro ao Cadastrar")
            
#Atualizar
@app.route("/route/<id>", methods=["PUT"])
def atualiza_dado(id):
    #pega a lista
    lista_classe = Listas_compras.query.filter_by(id=id).first()
    body = request.get_json()
    try:
        if('nome' in body):
            lista_classe .nome = body['name']
        if('quantidade' in body):
            lista_classe .email = body['quantidade']
        if('valor' in body):
            lista_classe .email = body['valor']
        db.session.add(lista_classe)
        db.session.commit()
        return gera_response(200,"lista", lista_classe.to_json(), "Atualizado com Sucesso")
    except Exception as e:
        print('erro', e)
        return gera_response(400,"lista", lista_classe.to_json(), "Erro ao atualizar")

#Deletar
@app.route("/lista/<id>", methods=["DELETE"])
def deletar_item(id):
    lista_classe = Listas_compras.query.filter_by(id=id).first()
    try:
        db.session.delete(lista_classe)
        db.session.commit()
        return gera_response(200, "lista", lista_classe.to_json(), "Deletada com Sucesso")
    except Exception as e:
        print("Erro", e)
        return gera_response("lista", {}, "Erro ao deletar")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):                                                      
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype=application()/json)
print(__name__)
if __name__ == '__main__':
    app.run(debug=True)