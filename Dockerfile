FROM python:3.6.0

MAINTAINER Luis Mayta <@slovacus>

COPY . /app/

# set working directory to /app/

WORKDIR /app/

# install python dependencies
RUN pip install -r /app/requirements/dev.txt
