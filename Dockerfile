FROM python:3.7


COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .


# CMD gunicorn --bind 0.0.0.0:$PORT wsgi

ENTRYPOINT ["python app.py"]