FROM python:3.9-slim

RUN apt-get update \
&& apt-get install -y --no-install-recommends git

COPY . .
RUN pip install --upgrade pip
RUN pip install -e .
ENTRYPOINT ["python", "-m", "fraud_transformer"]
