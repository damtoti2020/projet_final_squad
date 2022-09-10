FROM python:latest

MAINTAINER redhat

EXPOSE 8080

ADD python/cesar.py .

CMD ["python3", "cesar.py"]
