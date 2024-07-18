FROM python:3.8-slim

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME Converter

CMD ["python", "main.py"]