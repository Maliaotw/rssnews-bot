FROM python:3.7
COPY . /opt/bot/
WORKDIR /opt/bot/
# Set the locale
RUN cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN echo Asia/Taipei > /etc/timezone

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN pip install -r requirements.txt

ENTRYPOINT ["python","main.py"]


