""""
Copyright notice:
(c) Copyright 2024 RocketGate
All rights reserved.

The copyright notice must not be removed without specific, prior
written permission from RocketGate.

This software is protected as an unpublished work under the U.S. copyright
laws. The above copyright notice is not intended to effect a publication of
this work.
This software is the confidential and proprietary information of RocketGate.
Neither the binaries nor the source code may be redistributed without prior
written permission from RocketGate.

The software is provided "as-is" and without warranty of any kind, express, implied
or otherwise, including without limitation, any warranty of merchantability or fitness
for a particular purpose.  In no event shall RocketGate be liable for any direct,
special, incidental, indirect, consequential or other damages of any kind, or any damages
whatsoever arising out of or in connection with the use or performance of this software,
including, without limitation, damages resulting from loss of use, data or profits, and
whether or not advised of the possibility of damage, regardless of the theory of liability.
"""

import xml.sax
import http.client
import random
import errno
import socket
import ssl
from urllib.parse import urlsplit


class GatewayRequest:

    ######################################################################
    #
    #	Define constant hash values.
    #
    ######################################################################
    #
    VERSION_INDICATOR = "version"
    VERSION_NUMBER = "PY3.6"

    GATEWAY_URL = "gatewayURL"
    GATEWAY_SERVLET = "gatewayServlet"
    GATEWAY_CONNECT_TIMEOUT = "gatewayConnectTimeout"
    GATEWAY_SERVER = "gatewayServer"
    GATEWAY_PORTNO = "gatewayPortNo"
    GATEWAY_READ_TIMEOUT = "gatewayReadTimeout"

    DOCUMENT_BASE = "gatewayRequest"
    AMOUNT = "AMOUNT"
    AVS_CHECK = "AVSCHECK"
    BILLING_ADDRESS = "BILLINGADDRESS"
    BILLING_CITY = "BILLINGCITY"
    BILLING_COUNTRY = "BILLINGCOUNTRY"
    BILLING_STATE = "BILLINGSTATE"
    BILLING_ZIPCODE = "BILLINGZIPCODE"
    CARDNO = "CARDNO"
    CURRENCY = "CURRENCY"
    CUSTOMER_FIRSTNAME = "CUSTOMERFIRSTNAME"
    CUSTOMER_LASTNAME = "CUSTOMERLASTNAME"
    CVV2 = "CVV2"
    CVV2_CHECK = "CVV2CHECK"
    EMAIL = "EMAIL"
    EXPIRE_MONTH = "EXPIREMONTH"
    EXPIRE_YEAR = "EXPIREYEAR"
    IPADDRESS = "IPADDRESS"
    MERCHANT_ACCOUNT = "MERCHANTACCOUNT"
    MERCHANT_ACCOUNT_INDEX = "MERCHANTACCOUNTINDEX"
    MERCHANT_CUSTOMER_ID = "MERCHANTCUSTOMERID"
    MERCHANT_INVOICE_ID = "MERCHANTINVOICEID"
    MERCHANT_ID = "MERCHANTID"
    MERCHANT_PASSWORD = "MERCHANTPASSWORD"
    POSTING_IPADDRESS = "POSTINGIPADDRESS"
    REFERENCE_GUID = "REFERENCEGUID"
    TRANSACTION_TYPE = "TRANSACTIONTYPE"
    UDF01 = "UDF01"
    UDF02 = "UDF02"
    COF_FRAMEWORK = "COFFRAMEWORK"
    SS_NUMBER = "SSNUMBER"
    SCRUB = "SCRUB"
    IP2LOCATION_COUNTRY = "IP2LOCATIONCOUNTRY"
    IP2LOCATION_USAGE_TYPE = "IP2LOCATIONUSAGETYPE"
    BANK_COUNTRY = "BANKCOUNTRY"
    SCRUB_PROFILE = "SCRUBPROFILE"
    SCRUB_ACTIVITY = "SCRUBACTIVITY"
    SCRUB_NEGDB = "SCRUBNEGDB"
    BANK_CATEGORY = "BANKCATEGORY"
    BANK_NO_MEMBERSHIP = "BANKNOMEMBERSHIP"
    CARD_HASH = "CARDHASH"
    USERNAME = "USERNAME"
    CUSTOMER_PASSWORD = "CUSTOMERPASSWORD"
    AFFILIATE = "AFFILIATE"
    MERCHANT_DESCRIPTOR = "MERCHANTDESCRIPTOR"
    MERCHANT_DESCRIPTOR_TRIAL = "MERCHANTDESCRIPTORTRIAL"
    MERCHANT_DESCRIPTOR_SET = "MERCHANTDESCRIPTORSET"
    MERCHANT_DESCRIPTOR_TRIAL_SET = "MERCHANTDESCRIPTORTRIALSET"
    MERCHANT_DESCRIPTOR_CITY = "MERCHANTDESCRIPTORCITY"
    MERCHANT_SITE_ID = "MERCHANTSITEID"
    BILLING_TYPE = "BILLINGTYPE"
    MERCHANT_PRODUCT_ID = "MERCHANTPRODUCTID"
    REBILL_FREQUENCY = "REBILLFREQUENCY"
    REBILL_AMOUNT = "REBILLAMOUNT"
    REBILL_START = "REBILLSTART"
    REBILL_END_DATE = "REBILLENDDATE"
    REBILL_COUNT = "REBILLCOUNT"
    REBILL_TRANS_NUMBER = "REBILLTRANSNUMBER"
    REBILL_SUSPEND = "REBILLSUSPEND"
    REBILL_RESUME = "REBILLRESUME"
    REBILL_REACTIVATE = "REBILLREACTIVATE"
    REBILL_FEE = "REBILLFEE"
    EXISTING_CREDITS = "EXISTINGCREDITS"
    CUSTOMER_PHONE_NO = "CUSTOMERPHONENO"
    PARTIAL_AUTH_FLAG = "PARTIALAUTHFLAG"
    SUBMIT_ZERO_DOLLAR_AS_ONE_DOLLAR = "SUBMITZERODOLLARASONEDOLLAR"
    IOVATION_BLACK_BOX = "IOVATIONBLACKBOX"
    IOVATION_TRACKING_NO = "IOVATIONTRACKINGNO"
    IOVATION_DEVICE = "IOVATIONDEVICE"
    IOVATION_RESULTS = "IOVATIONRESULTS"
    IOVATION_RULE = "IOVATIONRULE"
    IOVATION_SCORE = "IOVATIONSCORE"
    IOVATION_RULE_COUNT = "IOVATIONRULECOUNT"
    IOVATION_RULE_TYPE_ = "IOVATIONRULETYPE_"
    IOVATION_RULE_REASON_ = "IOVATIONRULEREASON_"
    IOVATION_RULE_SCORE_ = "IOVATIONRULESCORE_"
    THREATMETRIX_SESSION_ID = "THREATMETRIXSESSIONID"
    REFERRER_URL = "REFERRERURL"
    GENERATE_POSTBACK = "GENERATEPOSTBACK"
    CLONE_CUSTOMER_RECORD = "CLONECUSTOMERRECORD"
    CLONE_TO_CUSTOMER_ID = "CLONETOCUSTOMERID"
    REFERRAL_NO = "REFERRALNO"
    REFERRING_MERCHANT_ID = "REFERRINGMERCHANTID"
    REFERRED_CUSTOMER_ID = "REFERREDCUSTOMERID"
    REFERRER_SUBMIT_FLAG = "REFERRERSUBMITFLAG"
    REFERRER_ALLOW_OVERRIDE_FLAG = "REFERRERALLOWOVERRIDEFLAG"
    REFERRER_PASSWORD = "REFERRERPASSWORD"
    CASCADE_RETRY_TYPE = "CASCADERETRYTYPE"
    CASCADE_ACCOUNT_LIST = "CASCADEACCOUNTLIST"
    CASCADE_TRIED_LIST = "CASCADETRIEDLIST"
    CASCADE_ERROR_CODES = "CASCADEERRORCODES"
    CASCADE_BANK_CODES = "CASCADEBANKCODES"
    RETRY_OMIT_CASCADE_ACCOUNTS = "RETRYOMITACCOUNTS"
    MAX_CASCADE_ATTEMPTS = "MAXCASCADEATTEMPTS"
    CASCADE_DISABLED = "CASCADEDISABLED"
    CASCADE_LAST_PROCESSOR = "CASCADELASTPROCESSOR"
    SUBMISSION_NUMBER = "SUBMISSIONNUMBER"
    PREFERRED_MERCHANT_ACCOUNT = "PREFERREDMERCHANTACCOUNT"
    CUSTOMER_CREATED_DATE = "customerCreatedDate"
    CUSTOMER_VELOCITY = "customerVelocity"
    CUSTOMER_VELOCITY_CURRENCY = "customerVelocityCurrency"
    XSELL_FLAG = "XSELLFLAG"
    XSELL_ORIGINAL_MERCHANT_CUSTOMER_ID = "XSELLORIGINALMERCHANTCUSTOMERID"
    XSELL_ORIGINAL_MERCHANT_ID = "XSELLORIGINALMERCHANTID"
    REBILL_FLAG = "REBILLFLAG"
    ORIGINAL_EXPIRE_MONTH = "originalExpireMonth"
    ORIGINAL_EXPIRE_YEAR = "originalExpireYear"
    EXPIRATION_RETRIES = "expirationRetries"
    DO_NOT_SEND_VOIDS = "doNotSendVoids"
    CVV_OVERRIDES_FOREIGN_AVS = "CVVOverridesForeignAVS"
    ACCT_COMPROMISED_SCRUB = "ACCTCOMPROMISEDSCRUB"
    PAYINFO_TRANSACT_ID= "PAYINFOTRANSACTID"
    BIN_ACCOUNT_EXCLUSIONS = "BINAccountExclusions"
    BIN_ROUTING_LIST = "BINRoutingList"
    BIN_ROUTING_INDEX = "BINRoutingIndex"
    CAPTURE_DAYS = "CAPTUREDAYS"
    FAILED_SERVER = "FAILEDSERVER"
    FAILED_GUID = "FAILEDGUID"
    FAILED_RESPONSE_CODE = "FAILEDRESPONSECODE"
    FAILED_REASON_CODE = "FAILEDREASONCODE"
    SITE_NO = "SITENO"
    BATCH_DURATION = "BATCHDURATION"
    BATCH_RECLOSE_GUID = "BATCHRECLOSEGUID"
    BATCH_UPLOAD = "BATCHUPLOAD"
    BATCH_TIME_OFFSET = "BATCHTIMEOFFSET"
    TEST_SITE = "TESTSITE"
    PARES = "PARES"
    USE_3D_SECURE = "USE3DSECURE"
    OMIT_RECEIPT = "OMITRECEIPT"
    OPERATION_TYPE = "OPERATION"
    FILENAME = "FILENAME"
    _3D_CHECK = "THREEDCHECK"
    _3D_ECI = "THREEDECI"
    _3D_CAVV_UCAF = "THREEDCAVVUCAF"
    _3D_XID = "THREEDXID"
    _3D_SIGNATURE = "THREEDSIGNATURE"
    _3D_PARESSTATUS = "THREEDPARESSTATUS"
    _3D_VERSTATUS = "THREEDVERSTATUS"
    _3D_CAVV_ALGORITHM = "THREEDCAVVALGORITHM"
    BROWSER_USER_AGENT = "BROWSERUSERAGENT"
    BROWSER_ACCEPT_HEADER = "BROWSERACCEPTHEADER"
    BROWSER_JAVA_ENABLED = "BROWSERJAVAENABLED"
    BROWSER_LANGUAGE = "BROWSERLANGUAGE"
    BROWSER_COLOR_DEPTH = "BROWSERCOLORDEPTH"
    BROWSER_SCREEN_HEIGHT = "BROWSERSCREENHEIGHT"
    BROWSER_SCREEN_WIDTH = "BROWSERSCREENWIDTH"
    BROWSER_TIME_ZONE = "BROWSERTIMEZONE"
    IS_3DSECURE_BYPASS = "is3DSecureBypass"
    IS_3DSECURE_AUTHREQ = "is3DSecureAuthReq"
    IS_3DSECURE_NOT_ENROLLED = "is3DSecureNotEnrolled"
    RETRY_3DSECURE_DECLINES = "retry3DSecureDeclines"
    RETRY_3DSECURE_FAILED_AUTHENTICATION = "retry3DSecureFailedAuthentication"
    ENABLE_3DS_PREPAID = "enable3DSPrepaid"
    IS_3DSECURE_INELIGIBLE = "is3DSecureIneligible"
    XSELL_MERCHANT_ID = "XSELLMERCHANTID"
    XSELL_MERCHANT_ACCOUNT = "XSELLMERCHANTACCOUNT"
    XSELL_MERCHANT_ACCOUNT_INDEX = "XSELLMERCHANTACCOUNTINDEX"
    XSELL_CUSTOMER_ID = "XSELLCUSTOMERID"
    XSELL_REFERENCE_XACT = "XSELLREFERENCEXACT"
    REBILL_AMOUNT_ON_3DS_LOOKUP = "REBILLAMOUNTON3DSLOOKUP"
    REFERENCE_SCHEME_TRANSACTION_ID = "SCHEMETRANID"
    REFERENCE_SCHEME_SETTLEMENT_DATE = "SCHEMESETTLEDATE"
    _3DSECURE_DF_REFERENCE_ID = "_3DSECURE_DF_REFERENCE_ID"
    _3DSECURE_REDIRECT_URL = "_3DSECURE_REDIRECT_URL"
    _3DSECURE_LOOKUP_SIGNATURE = "_3DSECURE_LOOKUP_SIGNATURE"
    _3DSECURE_DS_TRANSACTION_ID = "_3DSECURE_DS_TRANSACTION_ID"
    _3DSECURE_ACS_TRANSACTION_ID = "_3DSECURE_ACS_TRANSACTION_ID"
    _3DSECURE_CHALLENGE_MANDATED_INDICATOR = "_3DSECURE_CHALLENGE_MANDATED_INDICATOR"
    _3DSECURE_THREE_DS_SERVER_TRANSACTION_ID = "_3DSECURE_THREE_DS_SERVER_TRANSACTION_ID"
    IS_3DSECURE_FRICTIONLESS = "IS_3DSECURE_FRICTIONLESS"
    CARDINAL_API_KEY = "CARDINAL_API_KEY"
    CARDINAL_API_IDENTIFIER = "CARDINAL_API_IDENTIFIER"
    CARDINAL_SUB_PID = "CARDINAL_SUB_PID"
    CARDINAL_ORG_UNIT_ID = "CARDINAL_ORG_UNIT_ID"
    _3DSECURE_LOOKUP_CHALLENGE_INDICATOR = "_3DSECURE_LOOKUP_CHALLENGE_INDICATOR"

    _3DSECURE_ACS_WINDOW_SIZE = "_3DSECURE_ACS_WINDOW_SIZE"
    """
    An override field that a merchant can pass in to set the challenge window size to display to the end cardholder.
    
    The ACS will reply with content that is formatted appropriately to this window size to allow for the best user experience.
    
    The sizes are width x height in pixels of the window displayed in the cardholder browser window.
    
    The possible values are:
    
    - 01 (250x400)
    - 02 (390x400)
    - 03 (500x600)
    - 04 (600x400)
    - 05 (Full page)
    """

    PROCESSOR_3DS = "PROCESSOR3DS"
    DO_NOT_SEND_INCOMPLETE_3DS_AUTHENTICATION = "DO_NOT_SEND_INCOMPLETE_3DS_AUTH"
    MERCHANT_CASCADED_AUTH = "MERCHANTCASCADEDAUTH"
    FORCED_CARD_TYPE = "FORCED_CARD_TYPE"
    GOOGLE_PAY_TOKEN = "GOOGLEPAYTOKEN"
    NETWORK_TOKEN = "NETWORKTOKEN"
    NETWORK_TOKEN_EXPIRY_MONTH = "NETWORKTOKENEXPIRYMONTH"
    NETWORK_TOKEN_EXPIRY_YEAR = "NETWORKTOKENEXPIRYYEAR"
    NETWORK_CRYPTOGRAM = "NETWORKCRYPTOGRAM"
    NETWORK_CRYPTOGRAM_ECI = "NETWORKCRYPTOGRAMECI"
    NETWORK_TOKEN_REQUESTOR_ID = "NETWORKTOKENREQUESTORID"
    NETWORK_TOKENIZATION_DISABELD = "NETWORKTOKENIZATIONDISABELD"
    NETWORK_TOKEN_GUID = "networkTokenGuid"
    NETWORK_TOKEN_EXTERNAL_ID = "networkTokenExternalID"
    NETWORK_MERCHANT_ENTITY_ID = "networkMerchantEntityID"
    ALLOW_CARD_DEBIT_CREDIT = "ALLOW_CARD_DEBIT_CREDIT"
    _3D_VERSION = "THREEDVERSION"
    BANK_CARD_DEBIT_CREDIT = "BANK_CARD_DEBIT_CREDIT"
    SEND_MC_AUTH_INDICATOR = "SEND_MC_AUTH_INDICATOR"
    ONE_DOLLAR_FALLBACK_FOR_ZERO_DOLLAR_AUTH = "ONE_DOLLAR_FALLBACK_FOR_ZERO_DOLLAR_AUTH"
    NON_RELOADABLE_PREPAID_CARD = "NON_RELOADABLE_PREPAID_CARD"
    IS_3DS_LOOKUP_RETRY = "is3DSLookupRetry"
    USE_PRIMARY_SCHEMEID = "USEPRIMARYSCHEMEID"
    ACCOUNT_HOLDER = "accountHolder"
    ACCOUNT_NO = "accountNo"
    EMBEDDED_FIELDS_TOKEN = "embeddedFieldsToken"
    PAY_HASH = "cardHash"
    ROUTING_NO = "routingNo"
    SAVINGS_ACCOUNT = "savingsAccount"
    TRANSACT_ID = "referenceGUID"
    FAILURE_URL = "FAILUREURL"
    SUCCESS_URL = "SUCCESSURL"
    STYLE_SHEET = "style"
    STYLE_SHEET2 = "style2"
    STYLE_SHEET3 = "style3"
    TRANSLATIONS = "translations"
    SHOW_PAYMENT_FORM = "SHOW_PAYMENT_FORM"
    LANGUAGE = "LANGUAGE"
    ONCLICK_LOGO_URL = "onClickLogoURL"
    PAYMENT_LINK_TOKEN = "PAYMENTLINKTOKEN"

    """
    init__() - Constructor for class.
    """
    def __init__(self):
        self.parameterList = {}
        self.Set(GatewayRequest.VERSION_INDICATOR, GatewayRequest.VERSION_NUMBER)

    """
    Set() - Set a value in the parameter list.
    """
    def Set(self, key, value):
        self.Clear(key)  # Have key value? Delete it
        self.parameterList[key] = str(value)  # Save the value

    """
    Clear() - Clear a value in the parameter list.
    """
    def Clear(self, key):
        if key in self.parameterList:  # Have key value?
            del self.parameterList[key]  # Delete it

    """
    Get() - Get a value from the parameter list.
    """
    def Get(self, key):
        if key in self.parameterList:  # Have key value?
            return self.parameterList[key]  # Return the value
        return None  # Don't have a value

    """
    ToXML() - Create an XML document from the hash list.
    """
    def ToXML(self):

        #
        #	Build the document header.
        #
        xmlDocument = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        xmlDocument += "<gatewayRequest>"

        #
        #	Loop over each key-value pairs and create
        #	and open tag for the key.
        #
        for key, value in self.parameterList.items():
            xmlDocument += "<"
            xmlDocument += key
            xmlDocument += ">"

            #
            #	Clean up the value and add it to the tag.
            #
            myValue = str(value)  # In case it's not a string
            myValue = myValue.replace("&", "&amp;")
            myValue = myValue.replace("<", "&lt;")
            myValue = myValue.replace(">", "&gt;")
            xmlDocument += myValue

            #
            #
            #	Add the closing tag for this element.
            #
            xmlDocument += "</"
            xmlDocument += key
            xmlDocument += ">"

        #
        #	Close and return the document.
        #
        xmlDocument += "</gatewayRequest>"
        return xmlDocument  # Final document


class GatewayResponse(xml.sax.handler.ContentHandler):
    ######################################################################
    #
    #	Define constant hash values.
    #
    ######################################################################
    #
    VERSION_NO = "1.0"

    VERSION_INDICATOR = "version"
    DOCUMENT_BASE = "gatewayResponse"
    AUTH_NO = "authNo"
    AVS_RESPONSE = "avsResponse"
    CVV2_CODE = "cvv2Code"
    EXCEPTION = "exception"
    MERCHANT_ACCOUNT = "merchantAccount"
    REASON_CODE = "reasonCode"
    RESPONSE_CODE = "responseCode"
    REFERENCE_NO = "referenceNo"
    RETURNED_ACI = "returnedACI"
    TRANSACTION_TIME = "transactionTime"
    BANK_RESPONSE_CODE = "bankResponseCode"
    MERCHANT_ADVICE_CODE = "merchantAdviceCode"
    WIRECARD_3D_DATA = "INTERNAL0902091104"
    SCRUB_RESULTS = "scrubResults"
    APPROVED_AMOUNT = "approvedAmount"
    APPROVED_CURRENCY = "approvedCurrency"
    CARD_TYPE = "cardType"
    CARD_EXPIRATION = "cardExpiration"
    CARD_COUNTRY = "cardCountry"
    CARD_ISSUER_NAME = "cardIssuerName"
    CARD_ISSUER_PHONE = "cardIssuerPhone"
    CARD_ISSUER_URL = "cardIssuerURL"
    CARD_REGION = "cardRegion"
    CARD_DESCRIPTION = "cardDescription"
    CARD_DEBIT_CREDIT = "cardDebitCredit"
    PAY_TYPE = "payType"
    PAY_TYPE_CREDIT = "CREDIT"
    PAY_TYPE_DEBIT = "DEBIT"
    MERCHANT_CUSTOMER_ID = "merchantCustomerID"
    MERCHANT_INVOICE_ID = "merchantInvoiceID"
    ACS_URL = "acsURL"
    PAREQ = "PAREQ"
    CAVV_RESPONSE = "cavvResponse"
    ECI = "ECI"
    CACHED_3DSECURE_SCRUB = "cached3DSecureScrub"
    REBILL_END_DATE = "rebillEndDate"
    REBILL_DATE = "rebillDate"
    REBILL_AMOUNT = "rebillAmount"
    REBILL_CURRENCY = "rebillCurrency"
    REBILL_FREQUENCY = "rebillFrequency"
    LAST_BILLING_DATE = "lastBillingDate"
    LAST_BILLING_AMOUNT = "lastBillingAmount"
    JOIN_DATE = "joinDate"
    JOIN_AMOUNT = "joinAmount"
    REBILL_STATUS = "rebillStatus"
    LAST_REASON_CODE = "lastReasonCode"
    MERCHANT_SITE_ID = "merchantSiteID"
    MERCHANT_PRODUCT_ID = "merchantProductID"
    SCHEME_TRANSACTION_ID = "schemeTransactionID"
    SCHEME_SETTLEMENT_DATE = "schemeSettlementDate"
    BALANCE_AMOUNT = "balanceAmount"
    BALANCE_CURRENCY = "balanceCurrency"
    IOVATION_BLACK_BOX = "IOVATIONBLACKBOX"
    IOVATION_TRACKING_NO = "IOVATIONTRACKINGNO"
    IOVATION_DEVICE = "IOVATIONDEVICE"
    IOVATION_RESULTS = "IOVATIONRESULTS"
    IOVATION_ECHO= "IOVATIONECHO"
    IOVATION_SCORE = "IOVATIONSCORE"
    IOVATION_RULE_COUNT = "IOVATIONRULECOUNT"
    IOVATION_RULE_TYPE_ = "IOVATIONRULETYPE_"
    IOVATION_RULE_REASON_ = "IOVATIONRULEREASON_"
    IOVATION_RULE_SCORE_ = "IOVATIONRULESCORE_"
    IOVATION_SURE_SCORE = "IOVATIONSURESCORE"
    OPERATION = "operation"
    DATA = "data"
    IS_BANK_HARD_DECLINE = "isBankHardDecline"
    BATCH_NUMBER = "batchNumber"
    BATCH_SALES_COUNT = "batchSalesCount"
    BATCH_SALES_TOTAL = "batchSalesTotal"
    BATCH_CREDIT_COUNT = "batchCreditCount"
    BATCH_CREDIT_TOTAL = "batchCreditTotal"
    _3DSECURE_DEVICE_COLLECTION_JWT = "_3DSECURE_DEVICE_COLLECTION_JWT"
    _3DSECURE_DEVICE_COLLECTION_URL = "_3DSECURE_DEVICE_COLLECTION_URL"
    _3DSECURE_VERSION = "_3DSECURE_VERSION"
    _3DSECURE_STEP_UP_URL = "_3DSECURE_STEP_UP_URL"
    _3DSECURE_STEP_UP_JWT = "_3DSECURE_STEP_UP_JWT"
    PROCESSOR_3DS = "PROCESSOR3DS"
    _3DSECURE_CHALLENGE_INDICATOR = "_3DSECURE_CHALLENGE_INDICATOR"
    _3DSECURE_DS_TRANSACTION_ID = "_3DSECURE_DS_TRANSACTION_ID"
    _3DSECURE_PARESSTATUS = "_3DSECURE_PARESSTATUS"
    _3DSECURE_CAVV_UCAF = "_3DSECURE_CAVV_UCAF"
    _3DSECURE_CAVV_ALGORITHM = "_3DSECURE_CAVV_ALGORITHM"
    _3DSECURE_LOOKUP_SIGNATURE = "_3DSECURE_LOOKUP_SIGNATURE"
    _3DSECURE_XID = "_3DSECURE_XID"
    _3DSECURE_ACS_TRANSACTION_ID = "_3DSECURE_ACS_TRANSACTION_ID"
    _3DSECURE_THREE_DS_SERVER_TRANSACTION_ID = "_3DSECURE_THREE_DS_SERVER_TRANSACTION_ID"
    _3DSECURE_LOOKUP_CHALLENGE_INDICATOR = "_3DSECURE_LOOKUP_CHALLENGE_INDICATOR"
    _3DSECURE_CHALLENGE_MANDATED_INDICATOR = "_3DSECURE_CHALLENGE_MANDATED_INDICATOR"
    _3DSECURE_VERSTATUS = "_3DSECURE_VERSTATUS"
    _3DSECURE_LOOKUP_REFERENCE_GUID = "_3D_LOOKUP_REFERENCE_GUID"
    PARES = "PARES"
    BILLING_ADDRESS = "billingAddress"
    BILLING_CITY = "billingCity"
    BILLING_COUNTRY = "billingCountry"
    BILLING_STATE = "billingState"
    BILLING_ZIPCODE = "billingZipCode"
    CARD_BIN = "cardBin"
    CARDHOLDER_REASON_CODE_DESCRIPTION = "cardholderReasonCodeDescription"
    CUSTOMER_FIRSTNAME = "customerFirstName"
    CUSTOMER_LASTNAME = "customerLastName"
    EMAIL = "email"
    CARD_HASH = "cardHash"
    PAY_LAST_FOUR = "cardLastFour"
    PAYMENT_LINK_URL = "PAYMENT_LINK_URL"
    REASON_CODE_NAME = "reasonCodeName"
    RETRIEVAL_ID = "retrievalNo"
    TRANSACT_ID = "guidNo"
    SETTLED_AMOUNT = "approvedAmount"
    SETTLED_CURRENCY = "approvedCurrency"

    """
    init__() - Constructor for class.
    """
    def __init__(self):
        self.parameterList = {}  # Fresh list
        self.haveOpenTag = 0  # Haven't seen <gatewayResponse>
        self.valueBuffer = ""  # No value yet

    """
    Set() - Set a value in the parameter list.
    """
    def Set(self, key, value):
        if key in self.parameterList:  # Have key value?
            del self.parameterList[key]  # Delete it
        self.parameterList[key] = str(value)  # Save the value

    """
    Reset() - Clear all elements in a response.
    """
    def Reset(self):
        del self.parameterList  # Kill old list
        self.parameterList = {}  # Start with fresh list

    """
    Get() - Get a value from the parameter list.
    """
    def Get(self, key):
        if key in self.parameterList:  # Have key value?
            return self.parameterList[key]  # Return the value
        return None  # Don't have a value

    """
    SetFromXML() - Set values in a response object using an XML document.
    """
    def SetFromXML(self, xmlDocument):

        #
        #	Initialize the parsing.
        #
        self.haveOpenTag = 0  # Haven't tried to open
        self.valueBuffer = ""  # No value yet

        #
        #	Parse the input string.
        #
        try:
            xml.sax.parseString(xmlDocument, self)

        #
        #	If there was a parsing error, set the error codes
        #	and quit.
        #
        except xml.sax.SAXException as ex:
            self.Set(GatewayResponse.EXCEPTION, ex.getMessage() + \
                     ": " + xmlDocument)
            self.Set(GatewayResponse.RESPONSE_CODE, 3)
            self.Set(GatewayResponse.REASON_CODE, 400)

        #
        #	If there was some other type of exception, set the
        #	error codes and quit.
        #
        except:
            self.Set(GatewayResponse.EXCEPTION, "Unhandled exception: " + \
                     xmlDocument)
            self.Set(GatewayResponse.RESPONSE_CODE, 3)
            self.Set(GatewayResponse.REASON_CODE, 307)

    """
    startElement() - Handler for start of XML element.
    """
    def startElement(self, name, attrs):
        if name == GatewayResponse.DOCUMENT_BASE:  # Opening of document?
            self.haveOpenTag = 1  # Have seen open tag
        self.valueBuffer = ""  # Start with clean value

    """
    characters() - Handler for element string
    """
    def characters(self, data):
        if self.haveOpenTag:  # Seen open yet?
            self.valueBuffer += data

    """
    endElement() - Handler for end of XML element.
    """
    def endElement(self, name):
        if name != GatewayResponse.DOCUMENT_BASE:  # Opening of document?
            self.Set(name, self.valueBuffer)


class GatewayService:
    ######################################################################
    #
    #	Define constants
    #
    ######################################################################
    #
    ROCKETGATE_SERVLET = "/gateway/servlet/ServiceDispatcherAccess"
    ROCKETGATE_CONNECT_TIMEOUT = 10
    ROCKETGATE_READ_TIMEOUT = 90
    ROCKETGATE_PORTNO = 443
    ROCKETGATE_USER_AGENT = "RG Client - Python " + str(GatewayRequest.VERSION_NUMBER)

    LIVE_HOST = "gateway.rocketgate.com"
    LIVE_HOST_16 = "gateway-16.rocketgate.com"
    LIVE_HOST_17 = "gateway-17.rocketgate.com"
    TEST_HOST = "dev-gateway.rocketgate.com"

    """
    initialize() - Constructor for class.
    """
    def __init__(self):
        self.testMode = 0  # Default to live
        self.rocketGateDNS = GatewayService.LIVE_HOST
        self.rocketGateHost = GatewayService.LIVE_HOST
        self.rocketGateServlet = GatewayService.ROCKETGATE_SERVLET
        self.rocketGatePortNo = GatewayService.ROCKETGATE_PORTNO
        self.rocketGateConnectTimeout = GatewayService.ROCKETGATE_CONNECT_TIMEOUT
        self.rocketGateReadTimeout = GatewayService.ROCKETGATE_READ_TIMEOUT

    """
    SetTestMode() - Select test/development mode.
    """
    def SetTestMode(self, yesNo):
        if yesNo:  # Setting test mode?
            self.testMode = 1  # Set to test mode
            del self.rocketGateHost  # Delete old host list
            self.rocketGateHost = GatewayService.TEST_HOST
            self.rocketGateDNS = GatewayService.TEST_HOST
        else:
            self.testMode = 0  # Set to live mode
            del self.rocketGateHost  # Delete old host list
            self.rocketGateHost = GatewayService.LIVE_HOST
            self.rocketGateDNS = GatewayService.LIVE_HOST

    """
    SetHost() - Set the host used by the service
    """
    def SetHost(self, hostName):
        del self.rocketGateHost  # Delete old host list
        self.rocketGateHost = hostName  # Use this host
        self.rocketGateDNS = hostName

    """
    SetPortNo() - Set the port number used by the service.
    """
    def SetPortNo(self, portNo):
        try:
            value = int(portNo)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGatePortNo = value
        except:
            pass

    """
    SetServlet() - Set servlet used by the service.
    """
    def SetServlet(self, servlet):
        self.rocketGateServlet = servlet  # End point

    """
    SetConnectTimeout() - Set connection timeout
    """
    def SetConnectTimeout(self, timeout):
        try:
            value = int(timeout)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGateConnectTimeout = value
        except:
            pass

    """
    SetReadTimeout() - Set read timeout
    """
    def SetReadTimeout(self, timeout):
        try:
            value = int(timeout)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGateReadTimeout = value
        except:
            pass

    """
    SendTransaction() - Send a transaction to a named host.
    """
    def SendTransaction(self, serverName, request, response):

        #
        #	Gather overrides for transaction.
        #
        urlServlet = request.Get(GatewayRequest.GATEWAY_SERVLET)
        urlPortNo = request.Get(GatewayRequest.GATEWAY_PORTNO)

        #
        #	Determine the final servlet name.
        #
        if urlServlet == None:  # None specified?
            urlServlet = self.rocketGateServlet

        #
        #	Determine the final port number.
        #
        if urlPortNo == None:
            urlPortNo = self.rocketGatePortNo
        else:
            try:
                value = int(urlPortNo)  # Make sure this is numeric
            except:
                urlPortNo = self.rocketGatePortNo

        #
        #	Get the connection timeout.
        #
        connectTimeout = request.Get("gatewayConnectTimeout")
        if connectTimeout == None:
            connectTimeout = self.rocketGateConnectTimeout
        else:
            try:
                value = int(connectTimeout)  # Make sure this is numeric
            except:
                connectTimeout = self.rocketGateConnectTimeout

        #
        #	Get the read timeout.
        #
        readTimeout = request.Get("gatewayReadTimeout")
        if readTimeout == None:
            readTimeout = self.rocketGateReadTimeout
        else:
            try:
                value = int(readTimeout)  # Make sure this is numeric
            except:
                readTimeout = self.rocketGateReadTimeout

        #
        #	Prepare the values that will go into the post operation.
        #
        response.Reset()  # Clear any response data
        requestXML = request.ToXML()  # Get message string
        headers = {"Content-Type": "text/xml", \
                   "User-Agent": GatewayService.ROCKETGATE_USER_AGENT}

        #
        #	Create the HTTP handler and post our request.
        #
        try:
            connection = http.client.HTTPSConnection(serverName, urlPortNo, \
                                                     timeout=connectTimeout)
            connection.request("POST", urlServlet, requestXML, headers)
            connection.sock.settimeout(readTimeout)

            #
            #	Read the response.
            #
            results = connection.getresponse()
            body = results.read()  # Get the response data
            if isinstance(body, bytes):
                body = body.decode("utf-8")

            #
            #	If the response was not '200 OK', we must quit
            #
            if results.status != 200:
                response.Set(GatewayResponse.EXCEPTION, \
                             str(results.status) + ": " + body)
                response.Set(GatewayResponse.RESPONSE_CODE, 3)
                response.Set(GatewayResponse.REASON_CODE, 304)
                return 3  # System error

        #
        #	If there was a timeout, return an error.
        #
        except socket.timeout as ex:
            response.Set(GatewayResponse.EXCEPTION, str(ex))
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 301)
            return 3  # System error

        #
        #	If the read timed out, return an error.
        #
        except ssl.SSLError as ex:
            response.Set(GatewayResponse.EXCEPTION, str(ex))
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 303)
            return 3  # System error

        #
        #	If there was some other type of socket problemm,
        #	return an error.
        #
        except socket.error as ex:
            response.Set(GatewayResponse.EXCEPTION, str(ex))
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            exString = str(ex)
            if 'Connection refused' in exString:
                response.Set(GatewayResponse.REASON_CODE, 301)
            else:
                response.Set(GatewayResponse.REASON_CODE, 304)
            return 3  # System error

        #
        #	Catch general exceptions.
        #
        except Exception as ex:
            response.Set(GatewayResponse.EXCEPTION, str(ex))
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 304)
            return 3  # System error

        #
        #	Other exceptions must be caught too.
        #
        except:
            response.Set(GatewayResponse.EXCEPTION, "Unhandled POST exception")
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 304)
            return 3  # System error

        #
        #	Clean up the connection when we are all done.
        #
        finally:
            connection.close()  # Done with connection

        #
        #	Parse the response XML and return the response code.
        #
        response.SetFromXML(body)  # Set from response body
        responseCode = response.Get(GatewayResponse.RESPONSE_CODE)
        if responseCode == None:  # Don't have one?
            responseCode = 3  # System error
            response.Set(GatewayResponse.EXCEPTION, body)
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 400)
        return int(responseCode)  # Give back results

    """
    PerformTransaction() - Perform the transaction described in a gateway request.
    """
    def PerformTransaction(self, request, response):

        #
        #	If EMBEDDED_FIELDS_TOKEN is provided, send the request to the corresponding endpoint
        #
        fullUrl = request.Get(GatewayRequest.EMBEDDED_FIELDS_TOKEN)
        if fullUrl is not None:
            try:
                parsedUrl = urlsplit(fullUrl)
                request.Set(GatewayRequest.GATEWAY_SERVER, parsedUrl.hostname)
                request.Set(GatewayRequest.GATEWAY_SERVLET,
                            parsedUrl.path + ("?" + parsedUrl.query if parsedUrl.query is not None else ""))
                if parsedUrl.port is not None:
                    request.Set(GatewayRequest.GATEWAY_PORTNO, parsedUrl.port)
            except Exception as ex:
                response.Set(GatewayResponse.EXCEPTION, str(ex))
                response.Set(GatewayResponse.RESPONSE_CODE, 4)
                response.Set(GatewayResponse.REASON_CODE, 401)
                return 4  # Validation error: Invalid URL

        #
        #	If the request specifies a server name, use it.
        #	Otherwise, use the default.
        #
        server_name = request.Get(GatewayRequest.GATEWAY_SERVER)
        if server_name is not None:  # Override?
            server_list = [server_name]  # Use this name
        else:
            try:
                if self.rocketGateHost != GatewayService.LIVE_HOST:
                    server_list = [self.TEST_HOST]
                else:
                    server_list = socket.gethostbyname_ex(self.rocketGateHost)[2]
            except socket.gaierror:
                server_list = [GatewayService.LIVE_HOST_16, GatewayService.LIVE_HOST_17]

            server_list = [
                GatewayService.LIVE_HOST_16 if server == "69.20.127.91"
                else GatewayService.LIVE_HOST_17 if server == "72.32.126.131"
                else server
                for server in server_list
            ]

        #
        #	Clear any error tracking that may be leftover.
        #
        request.Clear(GatewayRequest.FAILED_SERVER)
        request.Clear(GatewayRequest.FAILED_RESPONSE_CODE)
        request.Clear(GatewayRequest.FAILED_REASON_CODE)
        request.Clear(GatewayRequest.FAILED_GUID)

        #
        #	Randomly pick an endpoint.
        #
        if len(server_list) > 1:  # Have multiples?
            index = random.randint(0, len(server_list) - 1)
            if index > 0:  # Want to change?
                swapper = server_list[0]  # Save the first one
                server_list[0] = server_list[index]
                server_list[index] = swapper  # And swap

        #
        #	Loop over the hosts and try to send the transaction
        #	to each host in the list until it succeeds or fails
        #	due to an unrecoverable error.
        #
        index = 0  # Start at first position
        while index < len(server_list):  # Loop over list
            results = self.SendTransaction(server_list[index], request, response)

            #
            #	If the transaction was successful, we are done
            #
            if results == 0:  # Success?
                return 1  # All done

            #
            #	If the transaction is not recoverable, quit.
            #
            if results != 3:  # Unrecoverable?
                return 0  # Must quit

            #
            #	Save any errors in the response so they can be
            # 	transmitted along with the next request.
            #
            request.Set(GatewayRequest.FAILED_SERVER, server_list[index])
            request.Set(GatewayRequest.FAILED_RESPONSE_CODE, \
                        response.Get(GatewayResponse.RESPONSE_CODE))
            request.Set(GatewayRequest.FAILED_REASON_CODE, \
                        response.Get(GatewayResponse.REASON_CODE))
            request.Set(GatewayRequest.FAILED_GUID, \
                        response.Get(GatewayResponse.TRANSACT_ID))
            index += 1  # Next index

        #
        #	If we ran out of places to send this, just quit.
        #
        return 0  # Must quit

    """
    PerformTargetedTransaction() - Send a transaction to a server based upon the GUID.
    """
    def PerformTargetedTransaction(self, request, response):

        #
        #	Clear any error tracking that may be leftover.
        #
        request.Clear(GatewayRequest.FAILED_SERVER)
        request.Clear(GatewayRequest.FAILED_RESPONSE_CODE)
        request.Clear(GatewayRequest.FAILED_REASON_CODE)
        request.Clear(GatewayRequest.FAILED_GUID)

        #
        #	This transaction must go to the host that processed a
        #	previous referenced transaction.  Get the GUID of the
        #	reference transaction.
        #
        referenceGUID = request.Get(GatewayRequest.REFERENCE_GUID)
        if referenceGUID == None:  # Don't have reference?
            response.Set(GatewayResponse.RESPONSE_CODE, 4)
            response.Set(GatewayResponse.REASON_CODE, 410)
            return 0  # And quit

        #
        #	Strip off the bits that indicate which server should
        #	be used.
        #
        if len(referenceGUID) > 15:  # Live servers?
            siteString = referenceGUID[0:2]  # Get first two digits
        else:
            siteString = referenceGUID[0:1]  # Get first digit

        #
        #	Try to turn the site string into a number.
        #
        try:
            siteNo = int(siteString, 16)  # Get site number
        except:  # Parsing error?
            response.Set(GatewayResponse.RESPONSE_CODE, 4)
            response.Set(GatewayResponse.REASON_CODE, 410)
            return 0  # And quit

        #
        #	Build the hostname to which the transaction should
        #	be directed.
        #
        server_name = request.Get("gatewayServer")
        if server_name is None:  # Don't have one?
            server_name = self.rocketGateDNS  # Start with default
            separator = server_name.find(".")  # Find first .
            if separator > 0:  # Did we find it?
                server_name = "{0}-{1}{2}".format(
                    server_name[0:separator],
                    str(siteNo),
                    server_name[separator:]
                )  # Full server name
        #
        #	Send the transaction to the specified host.
        #
        results = self.SendTransaction(server_name, request, response)
        if results == 0:  # Did server return 0?
            return 1  # This succeeded
        return 0  # This failed

    """
    PerformConfirmation() - Perform the confirmation pass that tells the server we have received the transaction reply.
    """
    def PerformConfirmation(self, request, response):

        #
        #	Verify that we have a transaction ID for the
        #	confirmation message.
        #
        confirmGUID = response.Get(GatewayResponse.TRANSACT_ID)
        if confirmGUID == None:  # Don't have reference?
            response.Set(GatewayResponse.EXCEPTION, \
                         "BUG-CHECK - Missing confirmation GUID")
            response.Set(GatewayResponse.RESPONSE_CODE, 3)
            response.Set(GatewayResponse.REASON_CODE, 307)
            return 0  # And quit

        #
        #	Add the GUID to the request and send it back to the
        #	original server for confirmation.
        #
        confirmResponse = GatewayResponse()  # Need a new response object
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_CONFIRM")
        request.Set(GatewayRequest.REFERENCE_GUID, confirmGUID)
        results = self.PerformTargetedTransaction(request, confirmResponse)
        if results:  # Success?
            return 1  # Yes - We are done

        #
        #	If the confirmation failed, copy the reason and response code
        #	into the original response object to override the success.
        #
        response.Set(GatewayResponse.RESPONSE_CODE, \
                     confirmResponse.Get(GatewayResponse.RESPONSE_CODE))
        response.Set(GatewayResponse.REASON_CODE, \
                     confirmResponse.Get(GatewayResponse.REASON_CODE))
        return 0  # And quit

    """
    PerformAuthOnly() - Perform an auth-only transaction.
    """
    def PerformAuthOnly(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_AUTH")
        results = self.PerformTransaction(request, response)
        if results:  # Success?
            results = self.PerformConfirmation(request, response)
        return results  # Return results

    """
    PerformTicket() - Perform a Ticket operation for a previous auth-only transaction.
    """
    def PerformTicket(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_TICKET")
        results = self.PerformTargetedTransaction(request, response)
        return results  # Return results

    """
    PerformPurchase() - Perform a complete purchase transaction.
    #
    """
    def PerformPurchase(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_PURCHASE")
        results = self.PerformTransaction(request, response)
        if results:  # Success?
            results = self.PerformConfirmation(request, response)
        return results  # Return results

    """
    PerformCredit() - Perform a Credit operation for a previous transaction.
    """
    def PerformCredit(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_CREDIT")

        #
        #	If this is a reference GUID, send the transaction to
        #	the appropriate server.  Otherwise use the normal
        #	transaction distribution.
        #
        referenceGUID = request.Get(GatewayRequest.REFERENCE_GUID)
        if referenceGUID != None:  # Have reference?
            results = self.PerformTargetedTransaction(request, response)
        else:
            results = self.PerformTransaction(request, response)
        return results  # Return results

    """
    PerformVoid() - Perform a Void operation for a previous transaction.
    """
    def PerformVoid(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_VOID")
        results = self.PerformTargetedTransaction(request, response)
        return results  # Return results

    """
    PerformCardScrub() - Perform scrubbing on a card/customer
    """
    def PerformCardScrub(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CARDSCRUB")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    """
    PerformRebillCancel() - Schedule cancellation of rebilling.
    """
    def PerformRebillCancel(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "REBILL_CANCEL")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    """
    PerformRebillUpdate() - Update terms of a rebilling.
    """
    def PerformRebillUpdate(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "REBILL_UPDATE")

        #
        #	If there is no prorated charge, just perform the update.
        #
        amount = request.Get(GatewayRequest.AMOUNT)
        if amount == None:  # No charge?
            results = self.PerformTransaction(request, response)
            return results  # Return results

        #
        #	If the amount will not result in a chage, just
        #	perform the update.
        #
        try:  # Check the amount
            value = float(amount)  # Make sure this is valid
            if value <= 0.0:  # Not chargeable?
                results = self.PerformTransaction(request, response)
                return results  # Return results
        except:  # Not a valid amount
            pass

        #
        #	If there is a charge, perform the update and confirm
        #	the charge.
        #
        results = self.PerformTransaction(request, response)
        if results:  # Success?
            results = self.PerformConfirmation(request, response)
        return results  # Return results

    """
    PerformCardUpload() - Upload card data to the servers.
    """
    def PerformCardUpload(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "CARDUPLOAD")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    """
    PerformLookup() - Perform GUID lookup
    """
    def PerformLookup(self, request, response):
        request.Set(GatewayRequest.TRANSACTION_TYPE, "LOOKUP")
        referenceGUID = request.Get(GatewayRequest.REFERENCE_GUID)
        if referenceGUID is not None:  # Have reference?
            results = self.PerformTargetedTransaction(request, response)
        else:
            results = self.PerformTransaction(request, response)
        return results

    """
    GenerateXsell() - Add an entry to the XsellQueue.
    """
    def GenerateXsell(self, request, response):
        # Apply the transaction type to the request
        request.Set(GatewayRequest.TRANSACTION_TYPE, "GENERATEXSELL")
        request.Set(GatewayRequest.REFERENCE_GUID, request.Get(GatewayRequest.XSELL_REFERENCE_XACT))

        if request.Get(GatewayRequest.REFERENCE_GUID) is not None:
            return self.PerformTargetedTransaction(request, response)
        else:
            return self.PerformTransaction(request, response)

    """
    BuildPaymentLink() - Create an embeddable RocketGate hosted payment link
    """
    def BuildPaymentLink(self, request, response) -> bool:
        if request.get(GatewayRequest.EMBEDDED_FIELDS_TOKEN) is not None:
            embedded_fields_token = request.get(GatewayRequest.EMBEDDED_FIELDS_TOKEN)
            gateway_url = embedded_fields_token.replace("EmbeddedFieldsProxy", "BuildPaymentLinkSubmit")
            request.set(GatewayRequest.GATEWAY_URL, gateway_url)
        else:
            request.set(GatewayRequest.GATEWAY_SERVLET, "/hostedpage/servlet/BuildPaymentLinkSubmit")

        self.PerformTransaction(request, response)

        return (response.get(GatewayResponse.RESPONSE_CODE) == GatewayCodes.RESPONSE_SUCCESS and
                response.get(GatewayResponse.PAYMENT_LINK_URL) is not None)


class GatewayCodes:
    # Static response codes
    RESPONSE_SUCCESS = 0  # Function succeeded
    RESPONSE_BANK_FAIL = 1  # Bank decline/failure
    RESPONSE_RISK_FAIL = 2  # Risk failure
    RESPONSE_SYSTEM_ERROR = 3  # Server/recoverable error
    RESPONSE_REQUEST_ERROR = 4  # Invalid request

    # Static reason codes
    REASON_SUCCESS = 0  # Function succeeded

    REASON_NOMATCHING_XACT = 100
    REASON_CANNOT_VOID = 101
    REASON_CANNOT_CREDIT = 102
    REASON_CANNOT_TICKET = 103
    REASON_DECLINED = 104
    REASON_DECLINED_OVERLIMIT = 105
    REASON_DECLINED_CVV2 = 106
    REASON_DECLINED_EXPIRED = 107
    REASON_DECLINED_CALL = 108
    REASON_DECLINED_PICKUP = 109
    REASON_DECLINED_EXCESSIVE = 110
    REASON_DECLINED_INVALID_CARDNO = 111
    REASON_DECLINED_INVALID_EXPIRATION = 112
    REASON_BANK_UNAVAILABLE = 113
    REASON_DECLINED_AVS = 117
    REASON_INVALID_REGION = 120
    REASON_USER_DECLINED = 123
    REASON_NETWORK_MISMATCH = 125
    REASON_CELLPHONE_BLACKLISTED = 126
    REASON_FULL_FAILURE = 127
    REASON_DECLINED_PIN = 129
    REASON_DECLINED_AVS_AUTOVOID = 150
    REASON_DECLINED_CVV2_AUTOVOID = 151
    REASON_INVALID_TICKET_AMT = 152
    REASON_INTEGRATION_ERROR = 154
    REASON_DECLINED_CAVV = 155
    REASON_UNSUPPORTED_CARDTYPE = 156
    REASON_DECLINED_RISK = 157
    REASON_INVALID_DEBIT_ACCOUNT = 158
    REASON_INVALID_USER_DATA = 159
    REASON_AUTH_HAS_EXPIRED = 160
    REASON_PREVIOUS_HARD_DECLINE = 161
    REASON_MERCHACCT_LIMIT = 162
    REASON_DECLINED_CAVV_AUTOVOID = 163
    REASON_DECLINED_STOLEN = 164
    REASON_BANK_INVALID_TRANSACTION = 165
    REASON_REFER_TO_MAKER = 166
    REASON_CVV2_REQUIRED = 167
    REASON_INVALID_TAX_ID = 169

    REASON_RISK_FAIL = 200
    REASON_CUSTOMER_BLOCKED = 201
    REASON_3DSECURE_AUTHENTICATION_REQUIRED = 202
    REASON_3DSECURE_NOT_ENROLLED = 203
    REASON_3DSECURE_INELIGIBLE = 204
    REASON_3DSECURE_REJECTED = 205
    REASON_RISK_CARD_CATEGORY = 206
    REASON_RISK_AVS_VS_ISSUER = 207
    REASON_RISK_DUPLICATE_MEMBERSHIP  = 208
    REASON_RISK_DUPLICATE_CARD = 209
    REASON_RISK_DUPLICATE_EMAIL = 210
    REASON_RISK_EXCEEDED_MAX_PURCHASE = 211
    REASON_RISK_DUPLICATE_PURCHASE = 212
    REASON_RISK_VELOCITY_CUSTOMER = 213
    REASON_RISK_VELOCITY_CARD = 214
    REASON_RISK_VELOCITY_EMAIL = 215
    REASON_IOVATION_DECLINE = 216
    REASON_RISK_VELOCITY_DEVICE = 217
    REASON_RISK_DUPLICATE_DEVICE = 218
    REASON_RISK_1CLICK_SOURCE = 219
    REASON_RISK_TOOMANYCARDS = 220
    REASON_AFFILIATE_BLOCKED = 221
    REASON_TRIAL_ABUSE = 222
    REASON_3DSECURE_BYPASS = 223
    REASON_RISK_NEWCARD_NODEVICE = 224
    REASON_3DSECURE_INITIATION = 225
    REASON_3DSECURE_FRICTIONLESS = 226
    REASON_3DSECURE_FRICTIONLESS_FAILED_AUTH = 227
    REASON_3DSECURE_SCA_REQUIRED = 228
    REASON_3DSECURE_CARDHOLDER_CANCEL = 229
    REASON_3DSECURE_ACS_TIMEOUT = 230
    REASON_3DSECURE_INVALID_CARD = 231
    REASON_3DSECURE_INVALID_TRANSACTION = 232
    REASON_3DSECURE_ACS_TECHNICAL_ISSUE = 233
    REASON_3DSECURE_EXCEEDS_MAX_CHALLENGES = 234

    REASON_DNS_FAILURE = 300
    REASON_UNABLE_TO_CONNECT = 301
    REASON_REQUEST_XMIT_ERROR = 302
    REASON_RESPONSE_READ_TIMEOUT = 303
    REASON_RESPONSE_READ_ERROR = 304
    REASON_SERVICE_UNAVAILABLE = 305
    REASON_CONNECTION_UNAVAILABLE = 306
    REASON_BUGCHECK = 307
    REASON_UNHANDLED_EXCEPTION = 308
    REASON_SQL_EXCEPTION = 309
    REASON_SQL_INSERT_ERROR = 310
    REASON_BANK_CONNECT_ERROR = 311
    REASON_BANK_XMIT_ERROR = 312
    REASON_BANK_READ_ERROR = 313
    REASON_BANK_DISCONNECT_ERROR = 314
    REASON_BANK_TIMEOUT_ERROR = 315
    REASON_BANK_PROTOCOL_ERROR = 316
    REASON_ENCRYPTION_ERROR = 317
    REASON_BANK_XMIT_RETRIES = 318
    REASON_BANK_RESPONSE_RETRIES = 319
    REASON_BANK_REDUNDANT_RESPONSES = 320
    REASON_WEBSERVICE_FAILURE = 321
    REASON_PROCESSOR_BACKEND_FAILURE = 322
    REASON_JSON_FAILURE = 323
    REASON_GPG_FAILURE = 324
    REASON_3DS_SYSTEM_FAILURE = 325
    REASON_USE_DIFFERENT_SERVER = 326

    REASON_XML_ERROR = 400
    REASON_INVALID_URL = 401
    REASON_INVALID_TRANSACTION = 402
    REASON_INVALID_CARDNO = 403
    REASON_INVALID_EXPIRATION = 404
    REASON_INVALID_AMOUNT = 405
    REASON_INVALID_MERCHANT_ID = 406
    REASON_INVALID_MERCHANT_ACCOUNT = 407
    REASON_INCOMPATIBLE_CARDTYPE = 408
    REASON_NO_SUITABLE_ACCOUNT = 409
    REASON_INVALID_REFGUID = 410
    REASON_INVALID_ACCESS_CODE = 411
    REASON_INVALID_CUSTDATA_LENGTH = 412
    REASON_INVALID_EXTDATA_LENGTH = 413
    REASON_INVALID_CUSTOMER_ID = 414
    REASON_TRANSACTION_NOT_FOUND = 415
    REASON_MISSING_INVOICE_ID = 416
    REASON_TRANSACTION_PENDING = 417
    REASON_INVALID_CURRENCY = 418
    REASON_INCOMPATABLE_CURRENCY = 419
    REASON_INVALID_REBILL_ARGS = 420
    REASON_INVALID_COUNTRY_CODE = 422
    REASON_INCOMPATABLE_COUNTRY = 424
    REASON_INVALID_ACCOUNT_NO = 426
    REASON_INVALID_ROUTING_NO = 427
    REASON_INVALID_LANGUAGE_CODE = 428
    REASON_INVALID_BANK_NAME = 429
    REASON_INVALID_BANK_CITY = 430
    REASON_INVALID_CUSTOMER_NAME = 431
    REASON_INVALID_BANKDATA_LENGTH = 432
    REASON_INVALID_PIN_NO = 433
    REASON_INVALID_PHONE_NO = 434
    REASON_INVALID_ACCOUNT_HOLDER = 435
    REASON_INCOMPATIBLE_DESCRIPTORS = 436
    REASON_INVALID_REFERRAL_DATA = 437
    REASON_INVALID_SITEID = 438
    REASON_DUPLICATE_INVOICE_ID = 439
    REASON_EXISTING_MEMBERSHIP  = 440
    REASON_INVOICE_NOT_FOUND = 441
    REASON_INVALID_BATCH_DURATION = 442
    REASON_MISSING_CUSTOMER_ID = 443
    REASON_MISSING_CUSTOMER_NAME = 444
    REASON_MISSING_CUSTOMER_ADDRESS = 445
    REASON_MISSING_CVV2 = 446
    REASON_MISSING_PARES = 447
    REASON_NO_ACTIVE_MEMBERSHIP = 448
    REASON_INVALID_CVV2 = 449
    REASON_INVALID_3D_DATA = 450
    REASON_INVALID_CLONE_DATA = 451
    REASON_REDUNDANT_SUSPEND_OR_RESUME = 452
    REASON_INVALID_PAYINFO_TRANSACT_ID = 453
    REASON_INVALID_CAPTURE_DAYS = 454
    REASON_INVALID_SUBMERCHANT_ID = 455
    REASON_INVALID_COF_FRAMEWORK = 458
    REASON_INVALID_REFERENCE_SCHEME_TRANSACTION = 459
    REASON_INVALID_CUSTOMER_ADDRESS = 460
    REASON_INVALID_CUSTOMER_ADDRESS = 460
    REASON_INVALID_CPF_FORMAT = 463
    REASON_INVALID_GOOGLE_PAY_TOKEN = 464
