# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
