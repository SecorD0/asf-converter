FROM python:3.9.7-slim

WORKDIR /program

COPY . .
RUN pip install --upgrade pip; \
    pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]