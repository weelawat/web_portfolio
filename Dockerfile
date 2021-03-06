FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
