FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (needed for psycopg2 compilation if using source, but we use binary)
# RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port (default 5000)
EXPOSE 5000

# Command to run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
