# routes.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import adicionar_empresa, listar_empresas

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    empresas = listar_empresas()
    return render_template('index.html', empresas=empresas)

@bp.route('/api/empresas', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_adicionar_empresa():
    if request.method == 'POST':
        data = request.get_json()
        cnpj = data.get('cnpj')
        nome = data.get('nome')

        if not cnpj or not nome:
            return jsonify({'erro': 'CNPJ e nome são obrigatórios'}), 400

        nova_empresa = adicionar_empresa(cnpj, nome)
        return jsonify(nova_empresa), 201

    elif request.method == 'GET':
        return jsonify(listar_empresas()), 200

    elif request.method == 'PUT':
        return jsonify({'mensagem': 'Método PUT ainda não implementado'}), 200

    elif request.method == 'DELETE':
        return jsonify({'mensagem': 'Método DELETE ainda não implementado'}), 200

    else:
        return jsonify({'mensagem': f'Método {request.method} não suportado'}), 405

@bp.route('/cadastrar', methods=['POST'])
def cadastrar_pelo_formulario():
    cnpj = request.form['cnpj']
    nome = request.form['nome']
    adicionar_empresa(cnpj, nome)
    return redirect(url_for('main.index'))
