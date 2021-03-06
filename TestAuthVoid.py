#! /usr/bin/env python
#
# Copyright notice:
# (c) Copyright 2020 RocketGate
# All rights reserved.
#
# The copyright notice must not be removed without specific, prior
# written permission from RocketGate.
#
# This software is protected as an unpublished work under the U.S. copyright
# laws. The above copyright notice is not intended to effect a publication of
# this work.
# This software is the confidential and proprietary information of RocketGate.
# Neither the binaries nor the source code may be redistributed without prior
# written permission from RocketGate.
#
# The software is provided "as-is" and without warranty of any kind, express, implied
# or otherwise, including without limitation, any warranty of merchantability or fitness
# for a particular purpose.  In no event shall RocketGate be liable for any direct,
# special, incidental, indirect, consequential or other damages of any kind, or any damages
# whatsoever arising out of or in connection with the use or performance of this software,
# including, without limitation, damages resulting from loss of use, data or profits, and
# whether or not advised of the possibility of damage, regardless of the theory of liability.
#

from RocketGate import *

request = GatewayRequest()
response = GatewayResponse()
service = GatewayService()

#
#	Setup the Auth-Only request.
#
request.Set(GatewayRequest.MERCHANT_ID, 1)
request.Set(GatewayRequest.MERCHANT_PASSWORD, "testpassword")
request.Set(GatewayRequest.CARDNO, "4111-1111-1111-1111")
request.Set(GatewayRequest.EXPIRE_MONTH, "02")
request.Set(GatewayRequest.EXPIRE_YEAR, "2030")
request.Set(GatewayRequest.AMOUNT, 10.97)
request.Set(GatewayRequest.AVS_CHECK, "IGNORE")
request.Set(GatewayRequest.MERCHANT_CUSTOMER_ID, "Customer-1")
request.Set(GatewayRequest.BILLING_ADDRESS, "317 Clydesdale Drive")
request.Set(GatewayRequest.BILLING_CITY, "Stephens City")
request.Set(GatewayRequest.BILLING_STATE, "Virginia")
request.Set(GatewayRequest.BILLING_ZIPCODE, "22655")
request.Set(GatewayRequest.BILLING_COUNTRY, "US")
request.Set(GatewayRequest.CVV2_CHECK, "IGNORE")
request.Set(GatewayRequest.CVV2, "999")
request.Set(GatewayRequest.EMAIL, "darcy@rocketgate.com")
request.Set(GatewayRequest.IPADDRESS, "68.224.133.117")
request.Set(GatewayRequest.SCRUB, "IGNORE")
#request.Set(GatewayRequest.SCRUB, "YES")

#
#      Setup test parameters in the service.
#
service.SetTestMode(1)

#
#      Perform the Auth-Only transaction.
#
status = service.PerformAuthOnly(request, response)
if (status):
    print ("Auth-Only succeeded")
    print ("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print ("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print ("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))
    print ("AuthNo: ", response.Get(GatewayResponse.AUTH_NO))
    print ("AVS: ", response.Get(GatewayResponse.AVS_RESPONSE))
    print ("CVV2: ", response.Get(GatewayResponse.CVV2_CODE))
    print ("CardHash: ", response.Get(GatewayResponse.CARD_HASH))
    print ("Account: ", response.Get(GatewayResponse.MERCHANT_ACCOUNT))
    print ("Scrub: ", response.Get(GatewayResponse.SCRUB_RESULTS))
else:
    print ("Auth-Only failed")
    print ("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print ("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print ("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))
    print ("Exception: ", response.Get(GatewayResponse.EXCEPTION))
    print ("Scrub: ", response.Get(GatewayResponse.SCRUB_RESULTS))
    exit()

#
#	Setup the ticket transaction.
#
request = GatewayRequest()
request.Set(GatewayRequest.MERCHANT_ID, 1)
request.Set(GatewayRequest.MERCHANT_PASSWORD, "testpassword")
request.Set(GatewayRequest.TRANSACT_ID, \
              response.Get(GatewayResponse.TRANSACT_ID))

#
#	Perform the void transaction.
#
status = service.PerformVoid(request, response)
if (status):
    print ("Void succeeded")
    print ("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print ("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print ("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))
    print ("AuthNo: ", response.Get(GatewayResponse.AUTH_NO))
else:
    print ("Void failed")
    print ("GUID: ", response.Get(GatewayResponse.TRANSACT_ID))
    print ("Response Code: ", response.Get(GatewayResponse.RESPONSE_CODE))
    print ("Reason Code: ", response.Get(GatewayResponse.REASON_CODE))

