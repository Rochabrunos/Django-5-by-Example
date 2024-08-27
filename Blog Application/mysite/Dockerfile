FROM python:3.12-slim

WORKDIR /usr/src/app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# creates a virtual environment
RUN pip install --upgrade pip

# copy project
COPY . .

RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]

ENTRYPOINT  ["/docker-entrypoint.sh"]

EXPOSE 8000
