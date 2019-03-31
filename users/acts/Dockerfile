FROM python:3.7-alpine3.7

ENV PYTHONUNBUFFERED 1
ENV TEAM_ID CC_200_228_209_203

WORKDIR /acts
RUN pip install --upgrade pip
COPY requirements.txt /acts/
RUN pip install -r requirements.txt
COPY . /acts/

EXPOSE 8000