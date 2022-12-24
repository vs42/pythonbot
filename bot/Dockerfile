FROM python:3.8-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD . /bot
WORKDIR /bot

RUN chmod +x /bot/run.py
ENV SERVER_PORT 5000
EXPOSE 5000
ENTRYPOINT ["python3", "/bot/run.py"]