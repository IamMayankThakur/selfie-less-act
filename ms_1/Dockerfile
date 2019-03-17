FROM python:3.7-alpine3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /ms1_app
RUN pip install --upgrade pip
COPY requirements.txt /ms1_app/
RUN pip install -r requirements.txt
COPY . /ms1_app/

EXPOSE 8000