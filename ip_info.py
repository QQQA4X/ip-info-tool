import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,regionName,city,zip,lat,lon,timezone,as,asname,proxy"
    r = requests.get(url).json()
    return r

def main():
    print("By Dev A4X")
    while True:
        ip = input("Enter IP (or 'exit' to quit): ").strip()
        if ip.lower() == "exit":
            break
        
        data = get_ip_info(ip)
        if data["status"] != "success":
            print("Invalid IP. Try again.\n")
            continue

        print(f"""
IP Information:
---------------
IP: {ip}
Code: {data['countryCode']}
Country: {data['country']}
Region: {data['regionName']}
City: {data['city']}
Latitude: {data['lat']}
Longitude: {data['lon']}
Zip Code: {data['zip']}
TimeZone: {data['timezone']}
ASN: {data['as'].split()[0] if data['as'] else 'N/A'}
AS Name: {data['asname']}
Proxy: {data['proxy']}

━━━━━━━━━━━━━━
By Dev A4X
""")
        
if __name__ == "__main__":
    main()
