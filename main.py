#   Importar o pandas(pip install pandas) / open py xl(pip install openpyxl) / twilio(pip install twilio)
import pandas as pd
from twilio.rest import Client
#   Twilio account.
account_sid = "AC44e3a52c2c2531432bc994b3a9e2c99b"
auth_token = "cf95d42b8a0562b516677d5104c4653c"
client = Client(account_sid, auth_token)
#   Abrir as listas/planilhas em excel.
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
#   Condição completa para validar o vendedor destaque e envio de um SMS confirmando a situação.
for mes in lista_meses:
    tabela_vedas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vedas['Vendas'] > 55000).any():
        vendedor = tabela_vedas.loc[tabela_vedas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vedas.loc[tabela_vedas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5532988586894",
            from_="+12482669650",
            body=f'No mês {mes} o vendedor {vendedor} atingiu a estimativa de vendas em torno de R${vendas}.')
        print(message.sid)
