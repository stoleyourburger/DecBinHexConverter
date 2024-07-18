FROM python:3.8-slim

WORKDIR /actiona-runner/_work/DecBinHexConverter/DecBinHexConverter

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME Converter

CMD ["python3", "main.py"]