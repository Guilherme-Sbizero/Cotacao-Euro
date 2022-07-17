# Use o comando pip install requests para fazer o download do requests

import requests

#Link publico com valor atual da cotação do Euro
url = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

# Busca os dados
response = requests.get(url)

# Se a busca funcionou, mostrar o valor
if response.status_code == 200:
    euro_value = response.json() ['EUR'] ['low']
    print(f'O valor do Euro é de R${euro_value}')
else:
    print('Erro ao buscar valor do Euro!')