# Use an official Python base image from the Docker Hub
FROM python:3.10-slim

# Install git
RUN apt-get -y update
RUN apt-get -y install git

# Copy the requirements.txt file and install the requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

# Set the entrypoint
ENTRYPOINT ["python", "main.py"]
