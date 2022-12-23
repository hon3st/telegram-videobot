FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "main.py"]
