FROM python:3.9-slim

RUN apt-get update \
&& apt-get install -y --no-install-recommends git

COPY . .
RUN pip install --upgrade pip
RUN pip install "kserve==0.12.1" "requests>=2.22.0" "numpy>=1.16.3"
ENTRYPOINT ["python", "-m", "simple_test.py"]