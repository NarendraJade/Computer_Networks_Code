import dns.resolver
def query_a_record(domain):
    result = dns.resolver.resolve(domain,'A')
    for ip in result:
        print(f"A record for {domain}: {ip}")
def query_mx_record(domain):
    result = dns.resolver.resolve(domain,'MX')
    for mx in result:
        print(f"MX record for {domain}: {mx.exchange} with priority {mx.preference}")
def query_txt_record(domain):
    result = dns.resolver.resolve(domain, 'TXT')
    for txt in result:
        print(f"TXT record for {domain}: {txt.to_text()}")
domain = "example.com"
query_a_record(domain)
query_mx_record(domain)
query_txt_record(domain)
