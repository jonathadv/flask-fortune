from python:3.6.6-stretch

RUN apt-get update && apt-get install python3-pip -y --force-yes && pip install pipenv

COPY . /app

WORKDIR /app

RUN pipenv install

CMD [ "pipenv", "run", "make", "start" ]

EXPOSE 8000