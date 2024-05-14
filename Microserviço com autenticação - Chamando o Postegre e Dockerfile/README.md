# Projeto MicroServiços

## Pré-requisitos

Antes de iniciar, certifique-se de que possui o Python instalado em sua máquina. Este projeto foi testado com Python 3.8.

## Instalação

Siga estes passos para instalar e configurar o seu projeto.

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

### Instale as dependencias

```bash
pip install -r requirements
```

### Suba o docker compose
```bash
docker-compose up -d
```

### Utilize a aplicação usando o token

Dentro do insominia ou postman, crie um modelo de autenticação bearer com a palavra "admin"

## Utilização da API

- /api/consulta
    essa rota serve para listagem dos produtos
    retorna um json de produtos

- /api/cadastro
    cadastra os produtos com nome e preço

- /api/consulta/<id>
    lista o produto com o id solicitado