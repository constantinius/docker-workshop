FROM python:3.8

# install dependencies
ADD requirements.txt .
RUN pip3 install -r requirements.txt

# Add app.py separately to allow more efficient layer caching
ADD ./app.py .

ENV FLASK_APP=app.py
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
