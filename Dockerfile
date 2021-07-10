FROM python:3

COPY . .

RUN pip3 install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s", "SOURCE"]