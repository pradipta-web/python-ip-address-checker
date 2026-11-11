import ipaddress

def check_ip(ip):

    try:
        address = ipaddress.ip_address(ip)

        print("\n========== IP ADDRESS INFORMATION ==========")

        print(f"IP Address : {address}")
        print(f"IP Version : IPv{address.version}")

        if address.is_private:
            print("IP Type    : Private IP")
        else:
            print("IP Type    : Public IP")

        if address.is_loopback:
            print("Category   : Loopback")

        if address.is_multicast:
            print("Category   : Multicast")

        print("============================================")

    except ValueError:
        print("\n[ERROR] Invalid IP Address!")


print("================================")
print("       IP ADDRESS CHECKER       ")
print("================================")

ip = input("Enter IP Address: ")

check_ip(ip)