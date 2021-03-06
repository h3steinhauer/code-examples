#!/usr/bin/python3

import requests
import base64
import json

# The hostname of the Reveal(x) 360 API. This hostname is displayed in Reveal(x)
# 360 on the API Access page under API Endpoint. The hostname does not
# include the /oauth/token.
HOST = "https://example.api.com"
# The ID of the REST API credentials.
ID = "abcdefg123456789"
# The secret of the REST API credentials.
SECRET = "123456789abcdefg987654321abcdefg"


def getToken():
    """
    Method that generates and retrieves a temporary API access token for Reveal(x) 360 authentication.

        Returns:
            str: A temporary API access token
    """
    auth = base64.b64encode(bytes(ID + ":" + SECRET, "utf-8")).decode("utf-8")
    print(auth)
    headers = {
        "Authorization": "Basic " + auth,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    r = requests.post(
        "%s/oauth2/token" % (HOST),
        headers=headers,
        data="grant_type=client_credentials",
    )
    return r.json()["access_token"]


def getDevices(token):
    """
    Method that sends a request to Reveal(x) 360 and authenticates the request with
    a REST API token. The request retrieves 100 active devices from the ExtraHop system.

        Returns
            list:  The list of active devices
    """
    headers = {"Authorization": "Bearer " + token}
    request_url = "%s/api/v1/devices" % (HOST)
    r = requests.get(request_url, headers=headers)
    return r.json()


def getDeviceGroups(token):
    """
    Method that sends a request to Reveal(x) 360 and authenticates the request with
    a REST API token. The request retrieves all device groups from the ExtraHop system.

        Returns
            list:  The list of device groups
    """
    headers = {"Authorization": "Bearer " + token}
    request_url = "%s/api/v1/devicegroups" % (HOST)
    r = requests.get(request_url, headers=headers)
    return r.json()


token = getToken()
devices = getDevices(token)
print(devices)
device_groups = getDeviceGroups(token)
print(device_groups)
