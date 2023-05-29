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

# environment
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64


CMD ["/bin/bash"]