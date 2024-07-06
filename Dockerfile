FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Add these lines for debugging
RUN pwd
RUN ls -la
RUN cat app.py

CMD ["python", "-u", "app.py"]