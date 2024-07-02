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

import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RocketGate import *

"""
Example Scenario:
$1.99 3-day trial which renews to $9.99/month subscription.
After 1 day the user wants to upgrade immediately to the full $9.99 subscription

The example code below will upgrade the membership immediately,
stop the trial period, bill the user $9.99,
and set the monthly rebill cycle starting today.
"""

# Setup required and testing variables
time_now = int(time.time())
cust_id = f"{time_now}.PythonTest"
inv_id = f"{time_now}.InstUpgrdTest"
merchant_id = "1"
merchant_password = "testpassword"

# Allocate the objects needed for the test
request = GatewayRequest()
response = GatewayResponse()
service = GatewayService()

# Setup the Purchase request
request.Set(GatewayRequest.MERCHANT_ID, merchant_id)
request.Set(GatewayRequest.MERCHANT_PASSWORD, merchant_password)

# Customer and invoice ID setup
request.Set(GatewayRequest.MERCHANT_CUSTOMER_ID, cust_id)
request.Set(GatewayRequest.MERCHANT_INVOICE_ID, inv_id)

# $9.99/month subscription with trial period
request.Set(GatewayRequest.CURRENCY, "USD")
request.Set(GatewayRequest.AMOUNT, "1.99")
request.Set(GatewayRequest.REBILL_START, "3")
request.Set(GatewayRequest.REBILL_FREQUENCY, "MONTHLY")
request.Set(GatewayRequest.REBILL_AMOUNT, "9.99")

# Card details
request.Set(GatewayRequest.CARDNO, "4111111111111111")
request.Set(GatewayRequest.EXPIRE_MONTH, "02")
request.Set(GatewayRequest.EXPIRE_YEAR, "2030")
request.Set(GatewayRequest.CVV2, "999")

# Customer information
request.Set(GatewayRequest.CUSTOMER_FIRSTNAME, "Joe")
request.Set(GatewayRequest.CUSTOMER_LASTNAME, "PythonTester")
request.Set(GatewayRequest.EMAIL, "pythontest@fakedomain.com")
request.Set(GatewayRequest.IPADDRESS, "127.0.0.1")

# Billing details
request.Set(GatewayRequest.BILLING_ADDRESS, "123 Main St")
request.Set(GatewayRequest.BILLING_CITY, "Las Vegas")
request.Set(GatewayRequest.BILLING_STATE, "NV")
request.Set(GatewayRequest.BILLING_ZIPCODE, "89141")
request.Set(GatewayRequest.BILLING_COUNTRY, "US")

# Risk/Scrub Request Setting
request.Set(GatewayRequest.SCRUB, "IGNORE")
request.Set(GatewayRequest.CVV2_CHECK, "IGNORE")
request.Set(GatewayRequest.AVS_CHECK, "IGNORE")

# Setup test parameters in the service and request
service.SetTestMode(True)

# Perform the Purchase transaction
if service.PerformPurchase(request, response):
    print("Purchase succeeded")
    print("Response Code:", response.Get(GatewayResponse.RESPONSE_CODE))
    print("Reason Code:", response.Get(GatewayResponse.REASON_CODE))
    print("Auth No:", response.Get(GatewayResponse.AUTH_NO))
    print("AVS:", response.Get(GatewayResponse.AVS_RESPONSE))
    print("CVV2:", response.Get(GatewayResponse.CVV2_CODE))
    print("GUID:", response.Get(GatewayResponse.TRANSACT_ID))
    print("Account:", response.Get(GatewayResponse.MERCHANT_ACCOUNT))
    print("Scrub:", response.Get(GatewayResponse.SCRUB_RESULTS))

    # Upgrade Membership
    request = GatewayRequest()
    request.Set(GatewayRequest.MERCHANT_ID, merchant_id)
    request.Set(GatewayRequest.MERCHANT_PASSWORD, merchant_password)
    request.Set(GatewayRequest.IPADDRESS, "127.0.0.1")

    request.Set(GatewayRequest.MERCHANT_CUSTOMER_ID, cust_id)
    request.Set(GatewayRequest.MERCHANT_INVOICE_ID, inv_id)

    request.Set(GatewayRequest.AMOUNT, "9.99")
    request.Set(GatewayRequest.REBILL_START, "AUTO")

    if service.PerformRebillUpdate(request, response):
        print("Upgrade succeeded")
    else:
        print("Upgrade failed")
        print("Response Code:", response.Get(GatewayResponse.RESPONSE_CODE))
        print("Reason Code:", response.Get(GatewayResponse.REASON_CODE))
else:
    print("Purchase failed")
    print("GUID:", response.Get(GatewayResponse.TRANSACT_ID))
    print("Response Code:", response.Get(GatewayResponse.RESPONSE_CODE))
    print("Reason Code:", response.Get(GatewayResponse.REASON_CODE))
    print("Exception:", response.Get(GatewayResponse.EXCEPTION))
    print("Scrub:", response.Get(GatewayResponse.SCRUB_RESULTS))
