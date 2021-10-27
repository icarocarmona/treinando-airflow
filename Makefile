
.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete
	
virtualenv/linux:
	virtualenv --always-copy --prompt '|> VirtualENV <| ' .venv
	env/bin/pip install -r src/requirements.txt
	@echo
	@echo "VirtualENV Setup Complete. Now run: source .venv/bin/activate"
	@echo

virtualenv/mac:
	python3 -m venv .venv
	pip install -r src/requirements.txt
	@echo
	@echo "VirtualENV Setup Complete. Now run: source .venv/bin/activate"
	@echo

install:
	sh scripts/install.sh

docker: clean
	docker build -t treinamento-airflow:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

docker-tag:
	docker tag treinamento-airflow:latest icarocarmona/treinamento-airflow:latest
	
docker-push:
	docker push treinamento-airflow:latest

airflow/start:
	@.venv/bin/airflow standalone

airflow/clean:
	@rm -rf ~/airflow/dags/*
	@rm -rf ~/airflow/plugins/*

deploy/plugins:	
	@cp -r ./airflow/plugins/* ~/airflow/plugins

deploy/dags:
	@cp -r ./airflow/dags/* ~/airflow/dags	

