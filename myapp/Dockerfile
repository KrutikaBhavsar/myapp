# We Use an official Python runtime as a parent image
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /music_service

# Set the working directory to /music_service
WORKDIR /music_service

# Copy the current directory contents into the container at /music_service
ADD . /music_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install wkhtmltopdf
RUN apt-get -y update && apt-get -y install wkhtmltopdf

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

