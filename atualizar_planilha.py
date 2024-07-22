import pandas as pd
import requests
import os
from tkinter import Tk, filedialog, messagebox, Button, Label

# Função para consultar o servidor Flask


def consultar_pagamento(cpf):
    url = 'http://127.0.0.1:5000/consultar'
    response = requests.post(url, data={'cpf': cpf})
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'Erro', 'data_pagamento': 'N/A', 'metodo_pagamento': 'N/A'}

# Função para gerar nome de arquivo com número sequencial


def gerar_nome_arquivo(base_name, ext, path):
    i = 1
    while os.path.exists(f"{path}/{base_name} {i}.{ext}"):
        i += 1
    return f"{path}/{base_name} {i}.{ext}"

# Função para selecionar a planilha dados_clientes


def selecionar_planilha():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Selecione a planilha dados_clientes",
        filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*"))
    )
    if file_path:
        label_planilha.config(text=f"Planilha selecionada: {
                              os.path.basename(file_path)}")
    else:
        label_planilha.config(text="Nenhuma planilha selecionada.")

# Função principal para gerar a planilha de fechamento


def gerar_planilha_fechamento():
    if not file_path:
        messagebox.showerror("Erro", "Nenhuma planilha selecionada.")
        return

    # Ler a planilha dados_clientes
    dados_clientes = pd.read_excel(file_path)

    # Criar uma lista para armazenar os dados da nova planilha
    dados_fechamento = []

    for _, row in dados_clientes.iterrows():
        cpf = row['CPF']
        resultado = consultar_pagamento(cpf)

        # Adicionar dados à lista
        dados_fechamento.append({
            'Nome': row['Nome'],
            'Valor': row['Valor'],
            'CPF': cpf,
            'Vencimento': row['Vencimento'],
            'Status': resultado['status'],
            'Data pagamento': resultado['data_pagamento'],
            'Método pagamento': resultado['metodo_pagamento']
        })

    # Criar um DataFrame para a planilha de fechamento
    df_fechamento = pd.DataFrame(dados_fechamento)

    # Definir o caminho para salvar a nova planilha
    path = os.path.dirname(file_path)
    file_name = gerar_nome_arquivo('planilha fechamento', 'xlsx', path)

    # Salvar a nova planilha
    df_fechamento.to_excel(file_name, index=False)
    messagebox.showinfo(
        "Sucesso", f"Planilha fechamento atualizada com sucesso: {file_name}")


# Configuração da interface gráfica
root = Tk()
root.title("Gerador de Planilha de Fechamento")

label_planilha = Label(root, text="Nenhuma planilha selecionada.")
label_planilha.pack(pady=10)

btn_selecionar = Button(
    root, text="Selecionar Planilha Dados Clientes", command=selecionar_planilha)
btn_selecionar.pack(pady=10)

btn_gerar = Button(root, text="Gerar Planilha Fechamento",
                   command=gerar_planilha_fechamento)
btn_gerar.pack(pady=10)

file_path = None

root.mainloop()
