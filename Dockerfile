
PIER-VIBE Dockerfile

Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments

FROM python:3.11-slim

LABEL maintainer="Samir Baladi <gitdeeper@gmail.com>"
LABEL description="PIER-VIBE: AI-Augmented Monitoring for Bridge Pier Safety"
LABEL version="1.0.0"
LABEL domain="Systems Safety & Engineering (AI-augmented)"
LABEL series="MARITIME-AI-01"

WORKDIR /app

Install system dependencies

RUN apt-get update && apt-get install -y --no-install-recommends 
    gcc 
    g++ 
    && rm -rf /var/lib/apt/lists/*

Copy requirements first for better caching

COPY requirements.txt .
COPY requirements-dev.txt .

Install Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

Copy the rest of the application

COPY . .

Install the package in development mode

RUN pip install -e .

Expose Streamlit port

EXPOSE 8501

Set environment variables

ENV PIER_VIBE_VIZ_ENABLED=true
ENV PIER_VIBE_VIZ_PORT=8501
ENV PIER_VIBE_LOG_LEVEL=INFO

Run the dashboard by default

CMD ["streamlit", "run", "examples/streamlit_live.py", "--server.port=8501", "--server.address=0.0.0.0"]
