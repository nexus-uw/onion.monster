FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GANDI_KEY=REPLACEME

#https://stackoverflow.com/questions/29663459/why-doesnt-python-app-print-anything-when-run-in-a-detached-docker-container
ENV PYTHONUNBUFFERED 1

# volume override creds + config

CMD [ "python", "manage.py", "runserver" ]