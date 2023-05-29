FROM gkdldhdl/ubuntu
LABEL maintainer="Siho Song"

# python 3.10.0
RUN apt-get install python3.10 -y && \
    apt-get install python3-pip -y && \
    rm -rf /usr/bin/python3 && \
    ln -s /usr/bin/python3.10 /usr/bin/python3 && \
    ln -s /usr/bin/python3.10 /usr/bin/python

# pip3 setting
RUN mkdir /root/.pip && \
    set -x \
    && { \
    echo '[list]'; \
    echo 'format = columns'; \
    } > /root/.pip/pip.conf && \
    pip3 install --upgrade pip && \
    pip3 install findspark pyspark

# workspace
WORKDIR /home/workspace

# environment
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

CMD ["/bin/bash"]