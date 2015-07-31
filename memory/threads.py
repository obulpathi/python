import gc
import os
import sys
import time
import requests
import threading

import pyrax
import pyrax.exceptions as exc
from memory_profiler import profile


pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.credentials.cfg")
pyrax.set_credential_file(creds_file)
dns = pyrax.cloud_dns


def worker():
    headers = {'X-Auth-Token': '793b5b9c6d8b4d3880d27ed6cfa96f92',
               'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Content-Length': 0}
    url = 'https://dns.api.rackspacecloud.com/v1.0/901255/domains'

    response = requests.get(url, headers=headers)
    print response

@profile(precision=3)
def foo():
    threads = []
    for i in range(100):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
        t.join()
        time.sleep(1)
    print('hi')

if __name__ == "__main__":
    foo()
