# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the contents of the local app directory to the container
COPY app/ /app/

# Define environment variables (if needed)
# ENV VARIABLE_NAME=value

# Expose the port that your application will run on
# EXPOSE 8443

# Run your application
CMD ["python", "main.py"]
