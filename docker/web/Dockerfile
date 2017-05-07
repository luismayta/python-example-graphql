FROM python:3.6.1

MAINTAINER Luis Mayta <@slovacus>

COPY requirements.txt /app/requirements.txt
COPY requirements /app/requirements/

# set working directory to /app/

WORKDIR /app/

# install python dependencies
RUN pip install -r /app/requirements/dev.txt
