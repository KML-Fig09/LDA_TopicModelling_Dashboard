# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy ONLY the necessary files
COPY requirements.txt .
COPY run.py .
COPY app/ ./app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run the app when container launches
CMD ["python", "run.py"]
