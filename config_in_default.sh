# Remember you're on Ubuntu Ola! - 
# File Location: /etc/default/elasticsearch

START_DAEMON=true
ES_USER=elasticsearch
ES_GROUP=elasticsearch
LOG_DIR=/var/log/elasticsearch
DATA_DIR=/var/lib/elasticsearch
WORK_DIR=/tmp/elasticsearch
CONF_DIR=/etc/elasticsearch
CONF_FILE=/etc/elasticsearch/elasticsearch.yml
RESTART_ON_UPGRADE=true


chown -R elasticsearch:elasticsearch /var/lib/elasticsearch/


