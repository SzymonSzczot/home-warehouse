# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster as env

# Set the working directory in the container to /app
WORKDIR /server

# Add the current directory contents into the container at /app
ADD . /server

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM env

# Make port 80 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
