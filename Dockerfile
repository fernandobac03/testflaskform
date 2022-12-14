FROM python:3.9

# Installing packages
RUN apt-get update

RUN pip install --upgrade pip

RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app

# Copy source code
COPY source .

# Install dependencies
RUN pip install -r requirements.txt

## Exec permission
# RUN chmod +x bootstrap.sh

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]