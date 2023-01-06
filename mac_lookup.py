#! /usr/bin/python3
import optparse
import requests


def main():
    """
    program looks up for the MAC address from the https://macaddress.io/ site with the provided MAC address and API_KEY for the site access.
    If valid parameters provides, Company's name for the MAC address will printed out to terminal else the response error codes.
    """
    parser = optparse.OptionParser(usage='usage: %prog -m <MAC address>  -a <API KEY>')
    parser.add_option('-m', '--mac_address', action="store", type="string", dest='mac_address',
                      help="please input MAC address")
    parser.add_option('-a', '--api_key', action="store", type="string", dest='api_key',
                      help="please API key for macaddress.io site")
    (options, args) = parser.parse_args()
    if not options.mac_address:  # if mac_address is not given
        parser.error('-m mac_address not given')
    if not options.api_key:  # if api_key is not given
        parser.error('-a api_key not given')

    http_url = f'https://api.macaddress.io/v1?apiKey={options.api_key}&output=json&search={options.mac_address}'
    mac_response = requests.get(http_url)

    if mac_response.status_code == 200:
        print(f"Company Name for the MAC address provided : {mac_response.json()['vendorDetails']['companyName']}.")
    elif mac_response.status_code == 400:
        print(
            f"Invalid parameters. Please check the mac address/API key.\nResponse from server : {mac_response.content}")
    elif mac_response.status_code == 401:
        print(f"Access restricted. Enter the correct API key.\nResponse from server : {mac_response.content}")
    elif mac_response.status_code == 402:
        print(f"Access restricted.Check the credits balance.\nResponse from server : {mac_response.content}")
    elif mac_response.status_code == 422:
        print(f"Invalid MAC or OUI address was received.\nResponse from server : {mac_response.content}")
    elif mac_response.status_code == 429:
        print(f"Too many requests. Try your call again later.\nResponse from server : {mac_response.content}")
    elif mac_response.status_code == 500:
        print(f"Internal server error. Try your call again.\nResponse from server : {mac_response.content}")
    else:
        print(
            f"Invalid response from  macaddress.io site HTTP code : {mac_response.status_code}\nResponse from server : {mac_response.content}")


if __name__ == "__main__":
    main()
