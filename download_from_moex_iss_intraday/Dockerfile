FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip cron
RUN python3 -m pip install --upgrade pip && pip3 install pandas

ADD crontab.cron .
RUN chmod 0644 crontab.cron
RUN crontab crontab.cron

ADD load_data_from_moex_iss.py .
RUN chmod 0644 load_data_from_moex_iss.py

CMD ["cron", "-f"]
