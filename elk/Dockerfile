FROM java:latest
RUN yum clean all
RUN rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
COPY elk.repo /etc/yum.repos.d/elk.repo
RUN yum install -y logstash elasticsearch initscripts kibana filebeat python-urllib3 python-requests
COPY logstash.conf /etc/logstash/conf.d
COPY entryPoint.sh /tmp
COPY elasticsearch_jvm.options /etc/elasticsearch/jvm.options
COPY kibana_import_indexes.py /usr/local/bin
RUN chmod +x /tmp/entryPoint.sh /usr/local/bin/kibana_import_indexes.py
ENTRYPOINT /tmp/entryPoint.sh
