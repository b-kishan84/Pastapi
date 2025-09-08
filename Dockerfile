FROM python:3.8-alpine
WORKDIR /app
COPY . .

RUN install -r requirements.txt
CMD python main.py