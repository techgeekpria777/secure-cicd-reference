FROM python:3.12-slim

WORKDIR /app

# Copy requirements first so this layer caches unless deps change.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app after deps, so code changes don't bust the deps layer.
COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]