FROM python:alpine3.23
WORKDIR /app
COPY . .
RUN pip install -r /app/req.txt
EXPOSE 8080
CMD ["python", "/app/app.py"]