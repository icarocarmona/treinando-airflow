## ---- Build Image ----
FROM python:3.8 AS build

## Install pip dependecies
COPY src/requirements.txt .
RUN pip3 install --user -r requirements.txt

## ---- Final Image ----
FROM python:3.8.10-slim-buster

## Create unprivileged user
RUN useradd -m app -u 1000 -s /bin/bash -d /home/app

## Copy pip dependecies
COPY --from=build /root/.local /home/app/.local
ENV PATH=/home/app/.local/bin:$PATH

## Copying source code
COPY . /home/app

## Fix all permissions.
RUN chown -R 1000:1000 /home/app

## Config user and run directory
USER app
WORKDIR /home/app

ENTRYPOINT ["sh", "bin/entrypoint.sh"]
