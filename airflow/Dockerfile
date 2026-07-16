FROM apache/airflow:3.3.0

USER root

# Install Java (required by Spark)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

USER airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt