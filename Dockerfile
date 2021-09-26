#FROM python:3.9-slim
FROM python:3.9.7-slim

RUN apt-get update && apt-get install -y iputils-ping && apt-get install -y iproute2

COPY ./app /app-member-service/app
COPY ./requirements.txt /app-member-service

WORKDIR /app-member-service

RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "app.server.app:app", "--host=0.0.0.0", "--reload"]


