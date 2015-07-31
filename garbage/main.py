import gc

class Caching(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Service(object):
    def __init__(self, caching=[]):
        pass

class Provider(object):
    def __init__(self):
        pass

    def _process_caching_rules(self, caching_rules):
        for caching_rule in caching_rules:
            caching_rules.remove(caching_rule)

    def update(self, service_obj):
        caching = service_obj.caching

def main():
    service_obj = Service()
    provider = Provider()
    for i in range(4):
        service.caching.append(str(i), i)
    provider.update(service_obj)
    print service_obj.caching
