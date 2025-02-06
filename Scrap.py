# Certifique-se de instalar as dependências antes de rodar:
# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Entrada do usuário
oportunidade = input("Qual vaga você deseja? ")
oportunidade_tratada = oportunidade.replace(" ", "%20").lower()

# Construindo a URL corretamente
url = f"https://www.linkedin.com/jobs/search?keywords={oportunidade_tratada}&location=Brasil&geoId=106057199&f_TPR=r86400&position=1&pageNum=0"

print(f"Acessando URL: {url}\n")

# Fazendo a requisição
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    site = BeautifulSoup(response.text, "html.parser")
    print("Página carregada com sucesso!")
else:
    print(f"Erro ao acessar a página. Código: {response.status_code}")

# Para visualizar o HTML (remova o comentário abaixo se quiser ver o código-fonte da página)
# print(site.prettify())
