FROM python:3.10

WORKDIR /quiz_service

COPY . /quiz_service

RUN pip install -r requirements.txt

CMD ["python3.10", "main.py"]
