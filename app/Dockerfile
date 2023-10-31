# Use the official Python image as a base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy your project files to the container
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose any necessary ports (if applicable)
EXPOSE 80

# Command to run your application
CMD ["python", "main.py"]
