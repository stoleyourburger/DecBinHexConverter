FROM python:3.8-slim

WORKDIR /root/actions-runner/_work/DecBinHexConverter/DecBinHexConverter

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME Converter

CMD ["python", "main.py"]