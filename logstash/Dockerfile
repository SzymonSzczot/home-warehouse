ARG ELASTIC_VERSION

FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}

RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.5.jar -o /usr/share/logstash/logstash-core/lib/jars/postgresql-jdbc.jar
