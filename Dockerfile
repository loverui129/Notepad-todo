# Use official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Cppy all files from the current directory to container
COPY . . 

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app_SQL.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask app
CMD ["flask", "run"]