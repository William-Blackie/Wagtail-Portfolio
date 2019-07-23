# Use an official Python runtime as a parent image
FROM python:3.7
LABEL maintainer="contact@williamblackie.com"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/Wagtail-Blog
WORKDIR /code
RUN ls -al

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r config/requirements.txt
RUN pip install gunicorn
RUN ls -al

WORKDIR /code/wagtail_portfolio
