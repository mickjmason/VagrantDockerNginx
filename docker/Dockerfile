FROM alpine:latest
RUN apk update  &&  apk add nginx
RUN mkdir -p /usr/share/nginx/html
RUN mkdir -p /etc/nginx/sites-available/default
RUN mkdir -p /etc/nginx/sites-enabled
ADD index.html /usr/share/nginx/html/index.html
RUN chown -R 0644 /usr/share/nginx/html
RUN chown -R 0644 /etc/nginx/sites-available/default
ADD nginx.conf /etc/nginx/sites-available/default/nginx.conf
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN sed -i '$i\ \ \ \ \ \ \ \ include /etc/nginx/sites-enabled/default/*.*;' /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx
EXPOSE 18081
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]



