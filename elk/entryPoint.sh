#!/bin/sh

function add_index() {
  while true; do
    /usr/local/bin/kibana_import_indexes.py
    sleep 30
  done
}

service elasticsearch start
service logstash start
service filebeat start
echo "server.host: $( hostname -i )" >> /etc/kibana/kibana.yml
service kibana start
add_index &
tail -f /var/log/kibana/kibana.stdout
