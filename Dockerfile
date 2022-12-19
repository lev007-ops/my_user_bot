FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

VOLUME /my_user_bot_volume

CMD [ "python3", "main.py"]