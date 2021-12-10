[![CodeQL](https://github.com/icarocarmona/treinando-airflow/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/icarocarmona/treinando-airflow/actions/workflows/codeql-analysis.yml)

Este projeto tem como objetivo treinar o conhecimento com Airflow.


## Requisitos
- Linux (testado apenas em Ubuntu);
## Configurando o projeto

Crie o ambiente virtual do python, ao final da criação do ambiente será solicitado
 a execução do seguinte comando `source env/bin/activate`.

```sh
make virtualenv
```

# Install

## Local
Nessa instalação os arquivos do Airflow ficarão no diretório `~/airflow`.
Após a instalação o script cria as pasta *dags* e *plugins*.

```sh
make install
```

# Start

```sh
make airflow/start
```

## Docker

### Setting the right Airflow user

```sh
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
### Initialize the database

```sh
docker-compose up airflow-init
```
### Running Airflow

```sh
docker-compose up
```


## Antes de começar

Você precisa cadastrar a connection `reqres_default` no airflow para que o `MyCustomHttpHook` funcione corretamente, por isso você deve criar uma connection com os seguintes parâmetros:
- Conn Id: `reqres_default`;
- Host: `https://reqres.in`;

## UI Links
- Airflow: [localhost:8080](localhost:8080)

## Create User

**For Airflow >=2.0.0:**
```sh
airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

## Referências

[Running Airflow locally](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

[Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

