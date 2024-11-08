# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]