# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Clone the repository (Replace 'your-repository-url' with the actual URL of your repo)
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/musket-eer/opti-bike.git .

# Set up a virtual environment
RUN . virtualenv/bin/activate

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
