# Usa a imagem oficial do Python 3.11 (versão slim = mais leve)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro do container
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para dentro do container
COPY . .

# Define o comando que será executado quando o container iniciar
CMD ["python", "-u", "main.py"]