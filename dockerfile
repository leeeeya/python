FROM python:3

RUN apt-get vim

WORKDIR /usr/src/app

COPY ./test_dock.py .

CMD ["python", "./test_dock.py"]
