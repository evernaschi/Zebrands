# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code to the container
COPY . /code/app

# Execute the prestart.sh script only during the build process
# RUN bash /code/app/prestart.sh

# Expose the necessary port(s)
# EXPOSE 8000

# Start the backend application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
