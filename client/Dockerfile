FROM node:lts-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:alpine3.19
WORKDIR /app
COPY --from=build ./app/dist/* ./
RUN npm install -g http-server
CMD [ "http-server", "dist" ]