FROM python:3.7.4-stretch

COPY requirements.txt /requirements/requirements.txt
RUN pip install -r /requirements/requirements.txt
RUN mkdir /code
WORKDIR /code
