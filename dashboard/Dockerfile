FROM ubuntu:22.04

WORKDIR /app

COPY package*.json ./

RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install

COPY /src ./src/
COPY /public ./public/

CMD ["npm", "start"]
