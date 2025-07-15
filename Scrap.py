# linkedin_scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def tratar_entrada(texto):
    return texto.replace(" ", "%20").lower()

def construir_url(vaga):
    base_url = "https://www.linkedin.com/jobs/search"
    parametros = f"?keywords={vaga}&location=Brasil&geoId=106057199&f_TPR=r86400&position=1&pageNum=0"
    return base_url + parametros

def extrair_vagas(html):
    soup = BeautifulSoup(html, "html.parser")
    vagas = soup.find_all("div", class_="base-search-card__info")

    titulos, empresas, localizacoes = [], [], []

    for vaga in vagas:
        titulo = vaga.find("h3", class_="base-search-card__title")
        empresa = vaga.find("h4", class_="base-search-card__subtitle")
        local = vaga.find("span", class_="job-search-card__location")

        titulos.append(titulo.text.strip() if titulo else "")
        empresas.append(empresa.text.strip() if empresa else "")
        localizacoes.append(local.text.strip() if local else "")

    return pd.DataFrame({
        "Título da Vaga": titulos,
        "Empresa": empresas,
        "Localização": localizacoes
    })

def main():
    print("🔎 Buscador de Vagas no LinkedIn (últimas 24h)")
    oportunidade = input("Qual vaga você deseja buscar? ")

    vaga_tratada = tratar_entrada(oportunidade)
    url = construir_url(vaga_tratada)

    print(f"\nAcessando URL: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Página carregada com sucesso. Extraindo vagas...\n")
        df = extrair_vagas(response.text)

        if df.empty:
            print("⚠️ Nenhuma vaga encontrada (pode ser limitação da requisição com requests).")
        else:
            print(df.head())
            nome_arquivo = f"vagas_{vaga_tratada}.csv"
            df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
            print(f"\n📁 Vagas salvas em: {nome_arquivo}")
    else:
        print(f"❌ Erro ao acessar a página (código: {response.status_code})")

if __name__ == "__main__":
    main()
