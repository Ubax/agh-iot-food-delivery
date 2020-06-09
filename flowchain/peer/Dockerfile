FROM node:8.14-stretch

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json package.json

RUN npm cache clean --force && npm install

COPY . .

ENV HOST 192.168.0.2
ENV PORT 4444
#ENV PEER_ADDR 192.168.0.107
ENV PEER_PORT 4444

CMD node peer.js