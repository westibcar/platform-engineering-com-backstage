FROM python:3.12.10-alpine
LABEL maintainer="@uday"

COPY /uday_app/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./uday_app /uday_app

CMD python /uday_app/app.py
