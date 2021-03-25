# Lesson 2 - Small Web-app

This lesson we will create a Dockerfile for an existing web application.

- Fill the Dockerfile with the relevant commands.
  - Start by setting the base image to `python:3.8`
  - Add the `requirements.txt` and the `app.py` to the image
  - Install the dependencies (`pip3 install -r requirements.txt`)
  - Set the environment variable `FLASK_APP` to your `app.py`
  - (Expose the later used port `5000`)
  - Set the command to be run to `flask run --host=0.0.0.0`

- Bonus points:
  - You are still developing the application and expect to do some changes to the `app.py` and do regular rebuilds of the image. How can the Dockerfile be structured to minimize the necessary time for each rebuild?

- Build the image and tag it as `lesson-02`
- Run the image with the following parameters
  - Forward the internal port `5000` to the outward port `5000`
  - Run the image in interactive mode and allocate a pseudo-tty
