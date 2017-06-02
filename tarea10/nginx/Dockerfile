FROM nginx:alpine
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "fblupi <fblupi@correo.ugr.es>"

COPY uwsgi.conf /etc/nginx/conf.d/

RUN apk update && apk upgrade \
    && mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.old

COPY static /home/app/static/

CMD ["nginx", "-g", "daemon off;"]
