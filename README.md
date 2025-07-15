# 🔎 Scraper de Vagas do LinkedIn (Busca por Palavra-chave)

Este projeto é um script em Python para buscar vagas no LinkedIn com base em palavras-chave definidas pelo usuário. Ele simula uma busca automática pelas vagas mais recentes publicadas nas últimas 24 horas, usando requests, BeautifulSoup e pandas.

⚠️ Observação: O LinkedIn pode limitar ou bloquear scrapers. Como o conteúdo é carregado dinamicamente via JavaScript, este script pode não encontrar todas as vagas esperadas. Para resultados mais confiáveis, utilize Selenium.

---

## 🚀 Como usar

### 1. Clone o repositório

git clone https://github.com/seu-usuario/linkedin_scraper.git  
cd linkedin_scraper

### 2. Crie um ambiente virtual (opcional)

python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Execute o script

python linkedin_scraper.py

Digite o nome da vaga (ex: cientista de dados) quando solicitado. O script irá:

- Montar a URL de busca no LinkedIn  
- Fazer a requisição da página  
- Tentar extrair título, empresa e local das vagas  
- Exibir os primeiros resultados  
- Salvar os dados em um arquivo .csv (por exemplo: vagas_cientista%20de%20dados.csv)

---

## ✅ Requisitos

- Python 3.7 ou superior  
- Acesso à internet

---

## 📁 Estrutura do Projeto

linkedin_scraper/  
├── linkedin_scraper.py  
├── requirements.txt  
└── README.md

---

## 👤 Autor

Rafael Freitas de Paula  
https://github.com/RafaelFreitas1009

---

## 📝 Licença

MIT License
