FROM postgres

ARG USER=sas
ARG UID=1141
ARG GID=1141
ARG PW=Orion123
COPY checkandinstall.sh ../
RUN apt-get update -y \
    && apt-get install -y wget unzip \
    && useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd \
    && usermod -aG sudo sas \
    && wget https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip \
    && unzip dvdrental.zip \
    && rm dvdrental.zip
USER postgres

#  RUN sleep 30 \
#       && postgres -i 
#       && sleep 30 \
#       && createdb dvdrental
#  RUN pg_restore -U postgres -d dvdrental dvdrental.tar \
#       && rm dvdrental.tar \
#       && rm dvdrental.zip

  