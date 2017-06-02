FROM mvertes/alpine-mongo:latest
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "fblupi <fblupi@correo.ugr.es>"

COPY mongodb /etc/conf.d/

WORKDIR /root/

CMD [ "mongod" ]
