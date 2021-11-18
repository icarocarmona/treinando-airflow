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
## Docker
TBD


# Start

```sh
make airflow/start
```
Acesse o airflow em localhost:8080 em seu navegador e use admin como usuário e a senha estará em seu console.

## UI Links
- Airflow: [localhost:8080](localhost:8080)

## Referências

[Running Airflow locally](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)
