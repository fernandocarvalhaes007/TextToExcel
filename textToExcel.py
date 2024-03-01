import pandas as pd 
from datetime import datetime

def convert_to_date(date_str):
    return datetime.strptime(date_str, '%Y%m%d').strftime('%d/%m/%Y') if date_str else None


# Organize os dados de acordo com seu TXT
####################################
def processar_linha(linha):
    user_id = linha[0:10].strip().lstrip('0')
    name = linha[10:55].strip()
    order_id = linha[55:65].strip().lstrip('0') or None
    product_id = linha[65:75].strip().lstrip('0') or None
    valor_produto_str = linha[75:87].replace(' ', '')
    value = convert_to_float(valor_produto_str)
    date_str = line[87:95].strip()
    date = convert_to_date(date_str)

    return user_id, name, order_id, product_id, value, date

####################################


def convert_to_float(value_str):
    return float(value_str.replace(',', '.')) if value_str else 0.0


# Aqui carrega o arquivo TXT
caminho_arquivo = "DEFINA O CAMINHO DO SEU ARQUIVO TXT "
dados = []

with open(caminho_arquivo, 'r') as file:
    for line in file:
        dados.append(processar_linha(line))

# Organize os dados de acordo com seu TXT
df = pd.DataFrame(dados, columns=["User_ID", "Name", "Order_ID", "Product_ID", "Value", "Data_Compra"])

# Salvar em um arquivo Excel
caminho_saida_excel = r"INFORME O CAMINHO DE SAIDA PARA O ARQUIVO TXT"
df.to_excel(caminho_saida_excel, index=False)

print(f"Dados processados salvos em {caminho_saida_excel}")