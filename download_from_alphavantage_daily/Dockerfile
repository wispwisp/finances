FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip cron
RUN python3 -m pip install --upgrade pip && pip3 install \
    pandas

ADD crontab.cron .
RUN chmod 0644 crontab.cron
RUN crontab crontab.cron

ADD *.py ./
RUN chmod 0644 *.py

CMD ["cron", "-f"]
