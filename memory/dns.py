import gc
import os
import sys
import time
import requests

import pyrax
import pyrax.exceptions as exc
from memory_profiler import profile


pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.credentials.cfg")
pyrax.set_credential_file(creds_file)
dns = pyrax.cloud_dns


def get_domains():
    headers = {'X-Auth-Token': 'ee0a869233ed4fe7ac68f47dafdc4a0f',
               'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Content-Length': 0}
    url = 'https://dns.api.rackspacecloud.com/v1.0/901255/domains'

    for i in range(10000):
        response = requests.get(url, headers=headers)
        print i, response
        time.sleep(1)

@profile(precision=3)
def bar():
    get_domains()

def foo():
    #gc.disable()
    #gc.set_debug(gc.DEBUG_LEAK)
    #gc.set_threshold(10,0,0)

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

    domains = dns.list()
    print len(domains)
    #gc.collect()
    time.sleep(1)
    print("Garbage: ".format(gc.garbage))

if __name__ == "__main__":
    bar()
