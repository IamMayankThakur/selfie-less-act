FROM python:3.7-alpine3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /ms2_app
RUN pip install --upgrade pip
COPY requirements.txt /ms2_app/
RUN pip install -r requirements.txt
COPY . /ms2_app/

EXPOSE 8080