FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

WORKDIR /app/chat_project

EXPOSE 8000

CMD ["daphne", "-p", "8000", "chat_project.asgi:application"]