FROM python:3.9-slim
WORKDIR /app
COPY app.py .
# We use -u to make sure Python output shows up immediately in your terminal
CMD ["python", "-u", "app.py"]