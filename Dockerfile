# Base image
FROM python:3.9-slim

RUN pip install --upgrade pip

# Setting up working dir in container
WORKDIR /library

# Copy the current directory contents into the container at /app
COPY . /library

# Install dependencies mentioned in requirements.txt
RUN pip install -r requirements.txt


# Runing application and performing other required actions
RUN chmod +x start-all.sh
ENTRYPOINT /library/start-all.sh

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
