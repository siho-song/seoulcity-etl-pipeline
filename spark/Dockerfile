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

#scala 2.13 
RUN cd /opt && \
    wget https://downloads.lightbend.com/scala/2.13.0/scala-2.13.0.tgz && \ 
    tar -xvf scala-2.13.0.tgz && \
    mv scala-2.13.0 scala && \
    rm -rf scala-2.13.0.tgz

# spark-3.4.0-bin-hadoop3.
RUN cd /opt && \
    wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz && \
    tar -xvf spark-3.4.0-bin-hadoop3.tgz && \
    mv spark-3.4.0-bin-hadoop3 spark && \
    rm -rf spark-3.4.0-bin-hadoop3.tgz

RUN cd /home &&\
    mkdir entrypoints

COPY ./entrypoint/spark-entrypoint.sh /home/entrypoints
COPY ./conf/spark-env.sh /opt/spark/conf
COPY ./conf/spark-defaults.conf /opt/spark/conf
COPY ./conf/log4j.properties /opt/spark/conf


#hadoop-3.3.1-bin
RUN cd /opt && \
    wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz && \
    tar -xvzf hadoop-3.3.1.tar.gz && \
    mv hadoop-3.3.1 hadoop && \
    rm -rf hadoop-3.3.1.tar.gz

# system environment

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV SCALA_HOME=/opt/scala
ENV PATH $PATH:/
ENV PATH $PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$HADOOP_HOME/bin:$SCALA_HOME/bin
ENV PYSPARK_PYTHON=/usr/bin/python3


ENV SPARK_MODE=master
ENV SPARK_MASTER_HOST=localhost
ENV SPARK_MASTER_PORT=17077
ENV SPARK_MASTER_WEBUI_PORT=18080
    
# CMD , ENTRYPOINT
# CMD /bin/bash -c "tail -f /dev/null && ../entrypoints/spark-entrypoint.sh"
CMD ["/bin/bash"]
# ENTRYPOINT ["../entrypoints/spark-entrypoint.sh"]

