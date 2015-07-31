from __future__ import print_function

import os

import pyrax
import pyrax.exceptions as exc

auth_endpoint="http://localhost:8900/identity/v2.0"
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_setting("auth_endpoint", auth_endpoint)

# Pass credentials directly (replace with your credentials)
try:
    pyrax.set_credentials("yourUserName", "58c3efaf88dccdb98afee24f5376f4ae")
except exc.AuthenticationFailed:
    print("Did you remember to replace the credentials with your actual", end=' ')
    print("username and api_key?")
print("authenticated =", pyrax.identity.authenticated)
print()

dns = pyrax.cloud_dns

# find subdomain
domain_name = "abc.example.edu"
domain = dns.find(name=domain_name)
print("Domain created:", domain)

# create subdomain
#domain = dns.create(name=domain_name, emailAddress="sample@example.edu", ttl=900, comment="sample domain")
#print("Domain created:", domain)