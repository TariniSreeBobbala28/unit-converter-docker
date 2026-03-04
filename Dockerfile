FROM python:3.9-slim
WORKDIR /app
COPY webapp.py .
# This installs the UI library inside the container
RUN pip install streamlit
# This tells Docker to allow web traffic on port 8501
EXPOSE 8501
# Command to run the web app
CMD ["streamlit", "run", "webapp.py", "--server.port=8501", "--server.address=0.0.0.0"]