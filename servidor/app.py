from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar a planilha de clientes (simulando um banco de dados)


def carregar_dados_clientes():
    return pd.read_excel('C:/Users/tairo/Documents/Thiago/Projetos/verificador-de-pagamentos-automatizado/Planilhas/dados_clientes.xlsx')

# Salvar a planilha de clientes


def salvar_dados_clientes(df):
    df.to_excel('Planilha Dados Clientes.xlsx', index=False)


@app.route('/')
def home():
    return "Servidor Flask está rodando!"


@app.route('/consultar', methods=['POST'])
def consultar():
    cpf = request.form.get('cpf')

    # Carregar dados da planilha
    df_clientes = carregar_dados_clientes()

    # Verificar se o CPF está na planilha
    cliente = df_clientes[df_clientes['CPF'] == cpf]

    if cliente.empty:
        return jsonify({'status': 'Cliente não encontrado', 'data_pagamento': 'N/A', 'metodo_pagamento': 'N/A'})

    # Simular status e método de pagamento
    status_pagamento = "Pago"  # ou "Pendente"
    data_pagamento = "2024-07-20"  # Data simulada
    metodo_pagamento = "Cartão"  # ou "Pix"

    # Atualizar a planilha com o status e método de pagamento
    df_clientes.loc[df_clientes['CPF'] == cpf, ['Status', 'Data pagamento', 'Método pagamento']] = [
        status_pagamento, data_pagamento, metodo_pagamento]
    salvar_dados_clientes(df_clientes)

    return jsonify({
        'status': status_pagamento,
        'data_pagamento': data_pagamento,
        'metodo_pagamento': metodo_pagamento
    })


if __name__ == "__main__":
    app.run(port=5000)
