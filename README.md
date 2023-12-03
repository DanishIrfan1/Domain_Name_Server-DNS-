# DNS and Reverse DNS Lookup Tool

This simple Python script provides a menu-driven interface for performing DNS and reverse DNS lookups.

## Prerequisites

- Python 3.x
- No additional dependencies required

## Usage

1. Clone the repository or download the `dns_lookup.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `dns_lookup.py` file is located.
4. Run the script using the following command:

    ```bash
    python dns_lookup.py
    ```

5. Follow the on-screen menu to perform DNS and reverse DNS lookups.

## Menu Options

1. **DNS Lookup**
   - Enter a host name, and the script will display the corresponding IP address and canonical name.

2. **Reverse DNS Lookup**
   - Enter an IP address, and the script will display the corresponding domain name (canonical name) and IP address.

3. **Exit**
   - Terminate the script.

## Error Handling

- The script includes basic error handling for socket-related exceptions.
- If an error occurs during the lookup process, an error message will be displayed.

## Example

```bash
$ python dns_lookup.py

 Menu:
 1. DNS 2. Reverse DNS 3. Exit

 Enter your choice
1

 Enter Host Name
google.com
Host Name: google.com
IP: 172.217.17.46


    Menu: 
 1. DNS 2. Reverse DNS 3. Exit 

 Enter your choice
2

 Enter IP address
172.217.17.46
IP: 172.217.17.46
Host Name: ams16s29-in-f46.1e100.net
```

