import socket

def main():
    n = 0
    while n != 3:
        print("\n Menu: \n 1. DNS 2. Reverse DNS 3. Exit \n")
        print("\n Enter your choice")
        n = int(input())

        if n == 1:
            try:
                print("\n Enter Host Name ")
                hname = input()
                address = socket.gethostbyname(hname)
                print("Host Name: " + socket.gethostbyaddr(address)[0])
                print("IP: " + address)
            except socket.error as e:
                print(e)

        elif n == 2:
            try:
                print("\n Enter IP address")
                ipstr = input()
                ia = socket.gethostbyaddr(ipstr)
                print("IP: " + ipstr)
                print("Host Name: " + ia[0])
            except socket.error as e:
                print(e)

if __name__ == "__main__":
    main()
