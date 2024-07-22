Aqui está um exemplo de README para o seu projeto:

---

# Verificador de Pagamentos Automatizado

Este projeto consiste em uma aplicação que automatiza o processo de verificação de pagamentos usando um servidor Flask para consulta e atualização de planilhas Excel. O sistema é composto por dois componentes principais:

1. **Código de Atualização de Planilha**
2. **Servidor Flask**

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

```
verificador-de-pagamentos-automatizado/
│
├── Planilhas/
│   ├── dados_clientes.xlsx
│   └── planilha_fechamento.xlsx
│
├── servidor/
│   └── app.py
│
└── atualizar_planilha.py
```

### 1. Código de Atualização de Planilha

O arquivo `atualizar_planilha.py` é responsável por:

- Ler a planilha `dados_clientes.xlsx` da pasta `Planilhas`.
- Consultar o servidor Flask para obter informações sobre o status de pagamento e método de pagamento.
- Atualizar a planilha com essas informações.
- Salvar a planilha atualizada com um número sequencial.

**Como executar:**

1. Certifique-se de que o servidor Flask está rodando na porta 5000.
2. Execute o script `atualizar_planilha.py` usando o comando:

   ```bash
   python atualizar_planilha.py
   ```

### 2. Servidor Flask

O servidor Flask, localizado no arquivo `app.py` dentro da pasta `servidor/`, realiza as seguintes funções:

- Carrega a planilha `dados_clientes.xlsx`.
- Permite a consulta do status de pagamento e método de pagamento via uma API REST.
- Atualiza a planilha com as informações consultadas.

**Como executar:**

1. Navegue até a pasta `servidor/`.
2. Execute o servidor Flask com o comando:

   ```bash
   python app.py
   ```

   O servidor Flask estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Requisitos

- Python 3.12 ou superior
- Bibliotecas Python: `Flask`, `pandas`, `requests`, `tkinter`

## Instruções de Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd verificador-de-pagamentos-automatizado
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install Flask pandas requests
   ```

## Uso

1. Inicie o servidor Flask executando `app.py` na pasta `servidor/`.

2. Execute o script `atualizar_planilha.py` para consultar e atualizar a planilha de dados.

3. Verifique a pasta `Planilhas/` para a planilha atualizada com um número sequencial.

## Observações

- Certifique-se de que o servidor Flask esteja rodando antes de executar o script de atualização da planilha.
- A planilha `dados_clientes.xlsx` deve conter as colunas `Nome`, `Valor`, `CPF`, e `Vencimento`.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se precisar de alguma modificação ou ajuste, é só avisar!
