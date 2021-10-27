#!/usr/bin/env bash
set -e
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.2.0
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.9
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.9.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

mkdir ${AIRFLOW_HOME}/plugins
mkdir ${AIRFLOW_HOME}/dags
