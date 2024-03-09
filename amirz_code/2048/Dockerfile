FROM nginx:1.23.3-alpine-slim
RUN apk --update add
RUN rm -f -r /usr/share/nginx/html/*
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
