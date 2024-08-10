import dns.zone
import dns.resolver
import dns.query
import argparse
import sys

def test_axfr_vulnerability(domain):
    try:
        ns_answers = dns.resolver.resolve(domain, 'NS')
        ns_servers = [str(ns) for ns in ns_answers]

        for ns in ns_servers:
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
                records = []
                for name, node in zone.nodes.items():
                    for rdataset in node.rdatasets:
                        records.append(f"{name} {rdataset.ttl} {dns.rdataclass.to_text(rdataset.rdclass)} {dns.rdatatype.to_text(rdataset.rdtype)} {' '.join(map(str, rdataset))}")
                return True, f"Domain {domain} is vulnerable (server {ns}):\n" + "\n".join(records)
            except Exception:
                continue
        return False, f"Domain {domain} is not vulnerable"
    except Exception:
        return False, f"Unable to check domain {domain}"

def test_domains_from_file(input_file, output_file):
    results = []

    try:
        with open(input_file, 'r') as file:
            domains = file.read().splitlines()

        for domain in domains:
            is_vulnerable, result = test_axfr_vulnerability(domain)
            if is_vulnerable:
                results.append(result)
                print(f"Vulnerable: {domain}")
            else:
                print(f"Not vulnerable: {domain}")

        with open(output_file, 'w') as file:
            file.write("\n\n".join(results))

        print(f"\nDetailed results for vulnerable domains have been saved to: {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred while processing the file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Test domains for AXFR vulnerability")
    parser.add_argument("input_file", help="Path to the file with the list of domains")
    parser.add_argument("output_file", help="Path to the file to save the results")
    args = parser.parse_args()

    test_domains_from_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
