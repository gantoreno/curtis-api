FROM python:3.7

COPY ./requirements.txt /curtis-server/requirements.txt

WORKDIR /curtis-server

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
