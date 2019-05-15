FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip && pip3 install \
    pandas lxml

ADD *.py ./
RUN chmod 0644 *.py
ENTRYPOINT ["/usr/bin/python3", "main.py"]
