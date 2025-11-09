# specifies the Parent Image from which you are building.
FROM python:3.9

# specify the working directory for the image
WORKDIR /code

# copying files
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

# requirements
RUN pip install -r /code/requirements.txt

# starting point
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]