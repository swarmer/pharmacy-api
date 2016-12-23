FROM ubuntu:16.04


# Install required packages
RUN apt-get update -y && \
    apt-get install -y \
        python3-dev \
        python3-pip \
        unzip


# Unpack the application code
COPY build/pharmacy-api.zip /tmp/pharmacy-api.zip
RUN unzip /tmp/pharmacy-api.zip -d /


RUN pip3 install -e /pharmacy-api


# Container settings
WORKDIR /pharmacy-api
EXPOSE 80
CMD pserve production.ini
