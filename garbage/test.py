import gc
import pprint

service = {}
service['caching'] = []
rule1 = "1"
rule2 = "2"
rule3 = "3"
service['caching'].append(rule1)
service['caching'].append(rule2)
service['caching'].append(rule3)

for cr_rule in service['caching']:
    for r in gc.get_referents(service):
        pprint.pprint(r)
