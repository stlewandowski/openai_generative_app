# Use an official Python runtime as a parent image
FROM python:3.10.14-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start Gunicorn
CMD ["gunicorn", "openai_generative_app.wsgi:application", "-w", "2", "-b", ":8000"]