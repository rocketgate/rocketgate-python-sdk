#! /usr/bin/env python

"""
Copyright notice:
(c) Copyright 2024 RocketGate
All rights reserved.

The copyright notice must not be removed without specific, prior
written permission from RocketGate.

This software is protected as an unpublished work under the U.S. copyright
laws. The above copyright notice is not intended to effect a publication of
this work. This software is the confidential and proprietary information of RocketGate.
Neither the binaries nor the source code may be redistributed without prior
written permission from RocketGate.

The software is provided "as-is" and without warranty of any kind, express, implied
or otherwise, including without limitation, any warranty of merchantability or fitness
for a particular purpose. In no event shall RocketGate be liable for any direct,
special, incidental, indirect, consequential or other damages of any kind, or any damages
whatsoever arising out of or in connection with the use or performance of this software,
including, without limitation, damages resulting from loss of use, data or profits, and
whether or not advised of the possibility of damage, regardless of the theory of liability.
"""

import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RocketGate import *

the_time = datetime.datetime.now().strftime("%Y%m%d.%H%M%S")

cust_id = the_time + ".PythonTest"
inv_id = the_time + ".RebillTest"
merch_id = "1"
merch_password = "testpassword"

request = GatewayRequest()
response = GatewayResponse()
service = GatewayService()

#
#	Setup the nly request.
#
request.Set(GatewayRequest.MERCHANT_ID, merch_id)
request.Set(GatewayRequest.MERCHANT_PASSWORD, merch_password)

request.Set(GatewayRequest.MERCHANT_CUSTOMER_ID, cust_id)
request.Set(GatewayRequest.MERCHANT_INVOICE_ID, inv_id)

# $1.99 3-day trial which renews to $9.99/month
request.Set(GatewayRequest.AMOUNT, 1.99)
request.Set(GatewayRequest.REBILL_AMOUNT, 9.99)
request.Set(GatewayRequest.CURRENCY, "USD")
request.Set(GatewayRequest.REBILL_START, "3")
request.Set(GatewayRequest.REBILL_FREQUENCY, "MONTHLY")

request.Set(GatewayRequest.CARDNO, "4111111111111111")
request.Set(GatewayRequest.EXPIRE_MONTH, "02")
request.Set(GatewayRequest.EXPIRE_YEAR, "2030")
request.Set(GatewayRequest.CVV2, "999")

request.Set(GatewayRequest.BILLING_ADDRESS, "123 Some Street")
request.Set(GatewayRequest.BILLING_CITY, "Las Vegas")
request.Set(GatewayRequest.BILLING_STATE, "Nevada")
request.Set(GatewayRequest.BILLING_ZIPCODE, "89141")
request.Set(GatewayRequest.BILLING_COUNTRY, "US")

request.Set(GatewayRequest.CUSTOMER_FIRSTNAME, "Monty")
request.Set(GatewayRequest.CUSTOMER_LASTNAME, "Python")
request.Set(GatewayRequest.EMAIL, "python_user@rocketgate.com")
request.Set(GatewayRequest.IPADDRESS, "68.224.133.117")

#
# Risk/Scrub Request Setting
#
request.Set(GatewayRequest.AVS_CHECK, "IGNORE")
request.Set(GatewayRequest.CVV2_CHECK, "IGNORE")
request.Set(GatewayRequest.SCRUB, "IGNORE")

#
#      Setup test parameters in the service.
#
service.SetTestMode(1)

#
#      Perform the Purchase transaction.
#

if service.PerformPurchase(request, response):
    print("Purchase succeeded")
    print("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))
    print("AuthNo: ", response.Get(GatewayResponse.AUTH_NO))
    print("AVS: ", response.Get(GatewayResponse.AVS_RESPONSE))
    print("CVV2: ", response.Get(GatewayResponse.CVV2_CODE))
    print("Card Hash: ", response.Get(GatewayResponse.CARD_HASH))
    print("Card Region: ", response.Get(GatewayResponse.CARD_REGION))
    print("Card Description: ", response.Get(GatewayResponse.CARD_DESCRIPTION))
    print("Account: ", response.Get(GatewayResponse.MERCHANT_ACCOUNT))
    print("Scrub: ", response.Get(GatewayResponse.SCRUB_RESULTS))
    print("Scrub: ", inv_id)
    print("Scrub: ", cust_id)

else:
    print("Purchase failed\n")
    print("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))
    print("Exception: ", response.Get(GatewayResponse.EXCEPTION))
    print("Scrub: ", response.Get(GatewayResponse.SCRUB_RESULTS))
    exit()
