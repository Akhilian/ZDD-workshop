# FROM python:3
# ADD api/ /api
# WORKDIR /api
# RUN apt-get update
# RUN pip install -r requirements.txt
# CMD python app.py

FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY ./api /api