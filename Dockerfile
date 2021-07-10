FROM python:3

COPY . .

RUN pip3 install --upgrade pip

CMD [ "python", "./SOURCE/CalculatorTests.py" ]