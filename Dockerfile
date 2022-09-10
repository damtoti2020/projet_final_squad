FROM python:latest

MAINTAINER redhat

EXPOSE 8080

ADD python/hello.py .

CMD ["python3", "cesar.py"]
