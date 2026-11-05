# Build lightweight, secure Python container
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment defaults
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_VERSION="v1.0.0" \
    APP_ENVIRONMENT="Production" \
    APP_COLOR="#10b981" \
    PORT=8080

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ .

# Expose port
EXPOSE 8080

# Run with Gunicorn production WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "2", "app:app"]
