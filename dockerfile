# Use an official Python runtime as a parent image
FROM python:3.13.3-slim AS base
WORKDIR /app

###################################################
# Stage: dev
# For development with auto-reload and file watching
###################################################
FROM base AS dev
# Install build tools for numpy and other packages
RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog[watchmedo] uvicorn
COPY . .
EXPOSE 8000
CMD ["watchmedo", "auto-restart", "--patterns=*.py", "--recursive", "--", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

###################################################
# Stage: prod
# For production deployment
###################################################
FROM base AS prod
# Install build tools for numpy and other packages
RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

