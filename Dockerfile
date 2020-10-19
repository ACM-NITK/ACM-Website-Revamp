FROM python:3.6-alpine
WORKDIR /home/
RUN apk update  \
    && apk add build-base \
    && apk add --no-cache libressl-dev musl-dev libffi-dev jpeg-dev zlib-dev \
    && apk add py3-pip \
    && pip install virtualenv \
    && virtualenv webenv \
    && source webenv/bin/activate \
    && pip install Django==2.2 \
    && pip install Pillow
EXPOSE 8000
WORKDIR /home/
RUN mkdir ACM-Website-Revamp
CMD /bin/sh; \
    cd /home; \
    source /home/webenv/bin/activate; \
    python /home/ACM-Website-Revamp/manage.py runserver 0.0.0.0:8000;
