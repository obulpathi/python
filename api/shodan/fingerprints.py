import shodan

api = shodan.Shodan(YOUR_API_KEY)

# Get the top 1,000 duplicated SSH fingerprints
results = api.count('port:22', facets=[('ssh.fingerprint', 1000)])

for facet in results['facets']['ssh.fingerprint']:
    print '%s --> %s' % (facet['value'], facet['count'])
