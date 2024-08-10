# DNS AXFR Vulnerability Scanner

This Python script is designed to test multiple domains for DNS AXFR (zone transfer) vulnerability. It provides a simple and efficient way to identify domains that are susceptible to unauthorized zone transfers, which can potentially expose sensitive information about the domain's DNS infrastructure.

## Features

- Test multiple domains from a file input
- Detect AXFR vulnerabilities in DNS servers
- Provide detailed zone information for vulnerable domains
- Save results to a file for further analysis
- Easy-to-use command-line interface

## Requirements

- Python 3.6+
- dnspython library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/elizarfish/AXFR.git
   cd dns-axfr-scanner
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a text file with a list of domains to test, one domain per line.

2. Run the script:
   ```
   python AXFR.py input_domains.txt output_results.txt
   ```
   Replace `input_domains.txt` with the path to your file containing the list of domains, and `output_results.txt` with the desired name for the output file.

3. The script will display a summary of vulnerable and non-vulnerable domains in the console and save detailed information about vulnerable domains to the output file.

## Output

- Console output: Shows which domains are vulnerable or not vulnerable.
- File output: Contains detailed DNS zone information for vulnerable domains.

## Disclaimer

This tool is for educational and ethical testing purposes only. Always ensure you have permission to test the domains in question. Unauthorized testing may be illegal in some jurisdictions.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/elizarfish/AXFR/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
