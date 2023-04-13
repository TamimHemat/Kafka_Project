FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install nginx

COPY default .

RUN cp default /etc/nginx/sites-available/default

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
