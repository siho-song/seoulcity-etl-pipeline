FROM gkdldhdl/ubuntu
LABEL maintainer="Siho Song"

# dependencies
RUN apt-get install dirmngr && \
    apt-get install gnupg && \
    apt-get install apt-transport-https && \
    apt-get install ca-certificates && \
    apt-get install software-properties-common

RUN curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor
   