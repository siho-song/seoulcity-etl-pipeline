#!/bin/bash

if [ "${SPARK_MODE}" == "master" ]; then
    ${SPARK_HOME}/sbin/start-master.sh &
fi

sleep 1

if [ "${SPARK_MODE}" == "worker" ]; then
    ${SPARK_HOME}/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} -c ${SPARK_WORKER_CORES} -m ${SPARK_WORKER_MEMORY} &
fi

sleep 1