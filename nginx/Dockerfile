
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY app.py .

ARG VERSION=dev
ENV VERSION=$VERSION

RUN python app.py

FROM nginx:alpine

COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -q --spider http://localhost || exit 1