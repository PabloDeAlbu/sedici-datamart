from postgis/postgis

RUN apt-get update && apt-get -y install git build-essential postgresql-server-dev-13

RUN git clone https://github.com/citusdata/pg_cron.git
RUN cd pg_cron && make && make install

RUN apt-get autoremove --purge -y && \
    apt-get clean && \
    apt-get purge
