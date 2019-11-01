# Dockerfile

# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /django_test
WORKDIR /django_test
ADD requirements.txt /django_test/
RUN pip install -r requirements.txt
ADD . /django_test/

# CMD [ "python", "-u", "./index.py" ]