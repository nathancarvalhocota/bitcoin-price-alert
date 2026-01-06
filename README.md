# Bitcoin Price Alert

Bot automatizado desenvolvido em Python que monitora o preço do Bitcoin em tempo real e envia alertas via Telegram. O projeto utiliza Docker para containerização e está deployado no Fly.io com pipeline de CI/CD configurado via GitHub Actions.

## Sobre o Projeto

Este projeto foi desenvolvido como uma aplicação prática para aprender e aplicar conceitos fundamentais de desenvolvimento backend moderno, incluindo:

- Programação assíncrona com Python
- Containerização com Docker
- Deploy em cloud (Fly.io)
- CI/CD com GitHub Actions
- Integração com APIs externas

## Funcionalidades

- Monitoramento automático do preço do Bitcoin em USD através da API do CoinGecko
- Verificações programadas em 6 horários: 06:00, 09:00, 12:00, 15:00, 18:00 e 21:00
- Notificações instantâneas via Telegram quando o preço é verificado
- Execução contínua 24/7 em ambiente cloud
- Deploy automático via CI/CD pipeline

## Tecnologias utilizadas

### Core

- **Python 3.11+** - Linguagem de programação principal
- **asyncio** - Programação assíncrona para operações I/O

### APIs e Bibliotecas

- **pycoingecko** - Cliente Python para a API do CoinGecko
- **python-telegram-bot** - Framework para interação com a Telegram Bot API
- **python-dotenv** - Gerenciamento de variáveis de ambiente

### DevOps e Infraestrutura

- **Docker** - Containerização da aplicação
- **Docker Compose** - Orquestração de containers para desenvolvimento local
- **Fly.io** - Plataforma cloud para deploy em produção
- **GitHub Actions** - Pipeline de CI/CD para deploy automático

### Descrição dos Principais Arquivos

**main.py**
Ponto de entrada da aplicação. Responsável por validar o valor alvo e inicializar o loop assíncrono de monitoramento.

**services/scheduler_service.py**
Implementa o loop de verificação que roda continuamente, checando o horário atual e acionando as verificações de preço nos momentos programados.

**services/crypto_service.py**
Contém a lógica de consulta à API do CoinGecko e formatação da mensagem de alerta.

**services/telegram_service.py**
Gerencia a conexão com a API do Telegram e o envio de mensagens, incluindo tratamento de erros.

**Dockerfile**
Define como a imagem Docker é construída, incluindo a imagem base, instalação de dependências e comando de execução.

**fly.toml**
Arquivo de configuração específico do Fly.io que define recursos, região de deploy e variáveis de ambiente.

## Pré-requisitos

Dependendo do método de execução escolhido, você precisará de:

### Para executar com Docker (recomendado):
- Docker Desktop instalado
- Git
- Token de bot do Telegram
- Chat ID do Telegram

### Para executar localmente sem Docker:
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Token de bot do Telegram
- Chat ID do Telegram

### Para fazer deploy no Fly.io:
- Conta no Fly.io
- Fly CLI instalado
- Git e GitHub (para CI/CD)

## Instalação e Configuração

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/SEU_USERNAME/bitcoin-price-alert.git
cd bitcoin-price-alert
```

### Passo 2: Obter Credenciais do Telegram

#### Criar um Bot no Telegram

1. Abra o Telegram e procure por `@BotFather`
2. Envie o comando `/newbot`
3. Siga as instruções para nomear seu bot
4. Copie o token fornecido (formato: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### Obter seu Chat ID

1. Procure por `@userinfobot` no Telegram
2. Envie qualquer mensagem
3. O bot responderá com seu Chat ID (um número)

### Passo 3: Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

## Como Usar

### Opção 1: Executar com Docker (Recomendado)

Esta é a forma mais simples e recomendada, pois garante que o ambiente de execução seja idêntico ao de produção.

```bash
# Construir a imagem
docker-compose build

# Iniciar o container em background
docker-compose up -d

# Ver logs em tempo real
docker-compose logs -f

# Parar o container
docker-compose down
```

### Opção 2: Executar Localmente com Python

Útil para desenvolvimento e debug.

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python main.py
```

## Deploy

### Deploy Manual no Fly.io

```bash
# Instalar Fly CLI
curl -L https://fly.io/install.sh | sh

# Fazer login
flyctl auth login

# Configurar secrets
flyctl secrets set TELEGRAM_BOT_TOKEN="seu_token"
flyctl secrets set TELEGRAM_CHAT_ID="seu_chat_id"

# Fazer deploy
flyctl deploy
```

### Deploy Automático via CI/CD

O projeto está configurado com GitHub Actions para deploy automático. Sempre que você fizer push para a branch `main`, o deploy acontece automaticamente.

#### Configurar CI/CD:

1. Obter token de autenticação do Fly.io:
```bash
flyctl auth token
```

2. No GitHub, vá para Settings > Secrets and variables > Actions

3. Adicione um novo secret:
   - Name: `FLY_API_TOKEN`
   - Value: Cole o token obtido

4. Pronto! Agora todo push na main fará deploy automático.

### Monitoramento

```bash
# Ver logs da aplicação
flyctl logs

# Ver status da aplicação
flyctl status

# Ver histórico de deploys
flyctl releases

# Acessar o container via SSH
flyctl ssh console
```

