FROM python:3.7.4-stretch

COPY requirements.txt requirements_dev.txt /requirements/
WORKDIR /requirements
RUN pip install -r requirements.txt -r requirements_dev.txt
RUN mkdir /code
WORKDIR /code
