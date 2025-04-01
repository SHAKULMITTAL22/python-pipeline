# Use an official Python 3.11 slim image as base.
FROM python:3.11-slim

# Install Java (required by Flink) and other build tools.
RUN apt-get update && \
    apt-get install -y default-jdk build-essential && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel.
RUN pip install --upgrade pip setuptools wheel
RUN pip install apache-flink pytest
WORKDIR /app
COPY . /app

# Default command: run the pipeline.
# You can change this to run tests instead, for example:
# CMD ["python", "-m", "unittest", "discover"]
# CMD ["python", "-m", "unittest", "discover", "-v"]

CMD ["python", "fraud_detection.py"]
