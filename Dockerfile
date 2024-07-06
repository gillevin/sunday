FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Create log directory
RUN mkdir -p /home/LogFiles && chmod 777 /home/LogFiles

CMD ["python", "-u", "app.py"]