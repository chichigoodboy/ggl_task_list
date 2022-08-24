FROM python:3.10.6-slim-buster

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./task_app /app/task_app
COPY main.py /app/main.py
COPY ./cli.py /app/cli.py
WORKDIR /app
ENV PYTHONPATH /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--http", "h11"]
