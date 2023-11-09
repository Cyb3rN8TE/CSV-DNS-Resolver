import socket
import csv

def get_mx_records(domain):
    try:
        mx_records = socket.getaddrinfo(domain, None, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        return [record[4][0] for record in mx_records]
    except socket.gaierror:
        return ["Not found"]

def get_records_from_csv(file_path, record_type):
    records = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                url = row[0].strip()
                if record_type == "A":
                    try:
                        ip_address = socket.gethostbyname(url)
                        records[url] = ip_address
                    except socket.gaierror:
                        records[url] = "Not found"
                elif record_type == "MX":
                    mx_records = get_mx_records(url)
                    records[url] = mx_records
    return records

def main():
    print("---------------------------------------------")
    print("CSV DNS Resolver")
    print("Version: 1.0.0")
    print("Author: Cyb3rN8TE 2023")
    print("The CSV DNS Resolver is a Python script that allows you to resolve DNS records for a list of domain names stored in a CSV file. It supports the retrieval of A records, MX records, and CNAME records")
    print("---------------------------------------------")
    print()

    file_path = input("Enter the CSV file path: ")
    record_type = input("Enter the DNS record type (A/MX/CNAME): ").upper()
    print()
    if record_type not in ["A", "MX", "CNAME"]:
        print("Invalid record type. Supported types are A, MX, and CNAME.")
        return
    result = get_records_from_csv(file_path, record_type)
    for url, record in result.items():
        print(f"{url}: {record}")
if __name__ == "__main__":
    main()
    print()

