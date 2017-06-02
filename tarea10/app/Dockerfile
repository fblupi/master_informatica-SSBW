FROM ubuntu:16.04
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "fblupi <fblupi@correo.ugr.es>"

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y git python-pip supervisor  \
    && pip install uwsgi  \
    && git clone https://github.com/fblupi/restaurantator.git /home/restaurantator  \
    && cd /home/restaurantator && pip install -r requirements.txt  \
    && apt-get remove -y git

EXPOSE 8000

COPY models.py /home/restaurantator/restaurantes/
COPY settings.py /home/restaurantator/sitio_web/
COPY app.ini /home/restaurantator/uwsgi/
COPY supervisord.conf /etc/

CMD ["supervisord", "-n"]
