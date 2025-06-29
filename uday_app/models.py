# models.py
empresas = []

def adicionar_empresa(cnpj, nome):
    empresa = {
        'cnpj': cnpj,
        'nome': nome
    }
    empresas.append(empresa)
    return empresa

def listar_empresas():
    return empresas
