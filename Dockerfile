FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Create log directory
RUN mkdir -p /tmp/log && chmod 777 /tmp/log

CMD ["sh", "-c", "python -u app.py & sleep 10 && ls -l /tmp/log && tail -f /tmp/log/application.log"]