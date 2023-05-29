FROM ubuntu:22.04
LABEL maintainer="SiHo Song"

# apt 설치시 입력요청 무시
ENV DEBIAN_FRONTEND=noninteractive

# apt 미러서버 미국(default) -> 한국 변경
RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

# 자주 사용하는 패키지 설치
RUN apt-get update && \
    apt-get install net-tools -y && \
    apt-get install iputils-ping -y && \
    apt-get install vim -y && \
    apt-get install wget -y

# # # workspace
WORKDIR /home/workspace

# # jdk
RUN apt-get install openjdk-8-jdk -y

# python 3.10.0
RUN apt-get install python3.10 -y && \
    apt-get install python3-pip -y && \
    rm -rf /usr/bin/python3 && \
    ln -s /usr/bin/python3.10 /usr/bin/python3 && \
    ln -s /usr/bin/python3.10 /usr/bin/python


# # spark-3.4.0-bin-hadoop3.
RUN mkdir /opt/spark && \
    cd /opt/spark && \
    wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz && \
    tar -xvf spark-3.4.0-bin-hadoop3.tgz && \
    mv spark-3.4.0-bin-hadoop3 spark && \
    rm -rf spark-3.4.0-bin-hadoop3.tgz

# # hadoop bin

# pip3 설정
RUN mkdir /root/.pip && \
    set -x \
    && { \
    echo '[list]'; \
    echo 'format = columns'; \
    } > /root/.pip/pip.conf && \
    pip3 install --upgrade pip && \
    pip3 install findspark pyspark

# environment
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH $PATH:/
ENV PATH $PATH:$JAVA_HOME/bin:$SPARK_HOME/bin
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook'
ENV PYSPARK_PYTHON=python3.8


