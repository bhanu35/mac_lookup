# mac_lookup

program looks up for the MAC address from the https://macaddress.io/ site with the provided MAC address and API_KEY for the site access.     If valid parameters provides, Company's name for the MAC address will printed out to terminal else the response error codes.

requirements: 
python3 {any platform should be fine}

Usage:

 mac_lookup.py -m <MAC address>  -a <API KEY>

Options:
  -h, --help            show this help message and exit
  -m MAC_ADDRESS, --mac_address=MAC_ADDRESS
                        please input MAC address
  -a API_KEY, --api_key=API_KEY
                        please API key for macaddress.io site

 Sample output:
    
with valid parameters:
./mac_lookup.py -m 44:38:39:ff:ef:57 -a <<YOUR API key>>
Company Name for the MAC address provided : Cumulus Networks, Inc

 with invalid parameters like API_KEY
./mac_lookup.py -m 44:38:39:ff:ef:57 -a at_teedvzPoJ8IJgYgwkLk1ZXSS14I
Access restricted. Enter the correct API key.
Response from server : b'{"error":"Access restricted. Enter the correct API key."}'
