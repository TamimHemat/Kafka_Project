FROM ubuntu:22.04
USER root
RUN apt -y update
RUN apt -y install python3
RUN apt -y install python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 create_database.py
CMD [ "python3", "app.py" ]
