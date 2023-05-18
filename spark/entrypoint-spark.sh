#!/bin/sh

# 스파크 마스터 실행
if [ ${SPARK_MODE} == "master" ]; then
    /bin/sh /spark/sbin/start-master.sh
fi

# 스파크 슬레이브 실행
if [ ${SPARK_MODE} == "worker" ]; then
    /bin/sh /spark/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} -c ${SPARK_WORKER_CORES} -m ${SPARK_WORKER_MEMORY}
fi
