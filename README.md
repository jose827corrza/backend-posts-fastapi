# TWEET FASTAPI

This API function will act like a place where you can login and leave your posts that everybody else will be able to see.

## Technologies

- FastApi

## Commands

Create an environment
> python3 -m venv env

Activate the environment

MacOS - Linux
> source env/bin/activate

Windows
> env/Scripts/activate

To set running the app with hot reloading, specifing the port and enabling the visibility to other devices into the same network.
> uvicorn main:app --reload --port 5001 --host 0.0.0.0

To generate a file which specifies the libraries that the project requires, run the following command
> pip freeze > requirements.txt

To install the libraries required by the project from the requirements file, run the following command
> pip install -r requirements.txt