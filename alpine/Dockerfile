
FROM python:3.12-alpine AS builder

WORKDIR /app


COPY app.py .

ARG VERSION=dev
ENV VERSION=$VERSION
FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /app /app

ENV VERSION=${VERSION}

EXPOSE 8080

CMD ["python", "app.py"]
