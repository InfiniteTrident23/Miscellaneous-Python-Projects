import socket
import requests
def get_local_ip():
    #Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #use socket to connect to external server
    s.connect(("8.8.8.8", 80)) #Google's DNS

    #Get local IP
    ip = s.getsockname()[0]

    s.close()

    return ip

def get_public_ip():
    #sending a request to httpbin.org to get public ip
    response = requests.get("https://httpbin.org/ip")
    return response.json()['origin']

def get_hostname_from_local_ip():
    local_ip = get_local_ip()
    try:
        hostename, _, _ = socket.gethostbyaddr(local_ip)
    except socket.herror:
        return "Host name not found"

print("Your local IP is:", get_local_ip())  
print("Your public IP is:", get_public_ip())
print("Your hostname is:", get_hostname_from_local_ip())