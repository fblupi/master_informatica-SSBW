FROM frolvlad/alpine-python3
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "fblupi <fblupi@correo.ugr.es>"

RUN apk update && apk upgrade \
    && apk add git supervisor gcc linux-headers python3-dev musl-dev freetype-dev libjpeg-turbo-dev lcms2-dev openjpeg-dev tiff-dev libwebp-dev libxml2-dev libxslt-dev zlib-dev \
    && pip install uwsgi  \
    && git clone https://github.com/fblupi/restaurantator.git /home/restaurantator  \
    && cd /home/restaurantator && pip install -r requirements.txt  \
    && apk del git gcc linux-headers

EXPOSE 8000

COPY models.py /home/restaurantator/restaurantes/
COPY settings.py /home/restaurantator/sitio_web/
COPY app.ini /home/restaurantator/uwsgi/
COPY supervisord.conf /etc/

CMD ["supervisord", "-n"]
