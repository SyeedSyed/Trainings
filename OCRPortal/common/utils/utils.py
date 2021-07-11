import random
import requests
import json


def getOTP():
    return random.randint(100000, 999999)


def sendSMS(message, contactno):

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=TXTIND&message=" + \
        message + "&route=v3&numbers=" + contactno
    headers = {
        'authorization': "Mnq2J240auosILQ9KJV5co4ifGDw1hd9XdMrKoVbL9MR5rU1uJHWPjYEFZ1k",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    dict_data = json.loads(response.text)
    return dict_data["return"]


# def sendSMS(message, contactno):
#     return True
