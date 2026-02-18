# Use official Python image (version 3.10 or above)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy app.py into container
COPY app.py .

# Install required dependency inside container
RUN pip install numpy

# Run the Python program when container starts
CMD ["python", "app.py"]
