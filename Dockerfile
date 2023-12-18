FROM python:3.11

WORKDIR /usr/src/app

RUN python3 -m venv venv

RUN . venv/bin/activate

COPY . .

RUN find . -type d -name __pycache__ -exec rm -r {} \+

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]