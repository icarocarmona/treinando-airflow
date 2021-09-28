
export AIRFLOW_HOME=$(pwd)/airflow

airflow initdb

airflow webserver

airflow scheduler

export AIRFLOW__CORE__KILLED_TASK_CLEANUP_TIME=604800

## Build

```sh
docker-compose up --build
```


## UI Links
- Airflow: [localhost:8080]()
