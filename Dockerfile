FROM python:3.7

MAINTAINER Mike Margetts <mmargetts@owletcare.com>

WORKDIR /usr/local/src

# Upgrade pip
RUN pip install --upgrade pip

# Copy code
COPY . .

# Install requirements
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
