import os
import re
from elasticsearch import Elasticsearch
from datetime import datetime
from elasticsearch.helpers import bulk

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

def parse_log_line(log_line):
    log_pattern = r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>[A-Z]+) (?P<url>[^\s]+) HTTP/(?P<http_version>[^\s]+)" (?P<status_code>\d+) (?P<bytes>\d+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)" "(?P<empty_field>[^"]*)"'
    match = re.match(log_pattern, log_line)
    if match:
        log_data = match.groupdict()
        timestamp = datetime.strptime(log_data['timestamp'], '%d/%b/%Y:%H:%M:%S %z')
        log_data['@timestamp'] = timestamp.isoformat()
        parsed_data = {
            "@timestamp": log_data['@timestamp'],
            "http.request.method": log_data['method'],
            "http.request.referrer": log_data['referrer'],
            "http.response.body.bytes": int(log_data['bytes']),
            "http.response.status_code": int(log_data['status_code']),
            "http.version": log_data['http_version'],
            "message": log_line.strip(),
            "source.address": log_data['ip'],
            "url.original": log_data['url'],
            "user_agent.original": log_data['user_agent']
        }
        return parsed_data
    else:
        return None

def send_logs_in_batches(log_file_path, batch_size=1000):
    index_name = 'server_logs'

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f"Created index: {index_name}")
    else:
        print(f"Index {index_name} already exists.")
        return

    with open(log_file_path, 'r') as f:
        bulk_data = []
        line_count = 0

        for log_line in f:
            log_data = parse_log_line(log_line)
            if log_data:
                document = {
                    "_op_type": "index",
                    "_index": index_name,
                    "_source": log_data
                }
                bulk_data.append(document)
                line_count += 1

            if len(bulk_data) >= batch_size:
                success, failed = bulk(es, bulk_data)
                print(f"Batch {line_count // batch_size} - Successfully indexed {success} documents.")
                print(f"Batch {line_count // batch_size} - Failed to index {failed} documents.")
                bulk_data = []

        if bulk_data:
            success, failed = bulk(es, bulk_data)
            print(f"Final Batch - Successfully indexed {success} documents.")
            print(f"Final Batch - Failed to index {failed} documents.")

log_file_path = '../data/access.log'
send_logs_in_batches(log_file_path, batch_size=1000)
