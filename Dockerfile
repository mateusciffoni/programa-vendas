# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de requirements.txt para o contêiner
COPY requirements.txt /app/

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código Python para o contêiner
COPY . /app/

# Comando para executar o programa
CMD ["python", "vendas_programa.py"]
