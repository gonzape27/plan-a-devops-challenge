FROM python:3.8.10-alpine

WORKDIR /usr/src/app

RUN addgroup -S plan-a-group && adduser -S plan-a-user -G plan-a-group --home "$(pwd)"

USER plan-a-user

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "server2.py"]
