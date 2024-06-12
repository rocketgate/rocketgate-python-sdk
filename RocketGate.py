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
import socket
import ssl
from urllib.parse import urlsplit


class GatewayRequest:

    VERSION_NUMBER = "PY3.6"
    VERSION_INDICATOR = "version"

    ######################################################################
    #
    #	Define constant hash values.
    #
    ######################################################################
    #

    ACCOUNT_HOLDER = "accountHolder"
    ACCOUNT_NO = "accountNo"
    ACCT_COMPROMISED_SCRUB = "ACCTCOMPROMISEDSCRUB"
    AFFILIATE = "AFFILIATE"
    ALLOW_CARD_DEBIT_CREDIT = "ALLOW_CARD_DEBIT_CREDIT"
    AMOUNT = "AMOUNT"
    AVS_CHECK = "AVSCHECK"
    BANK_CARD_DEBIT_CREDIT = "BANK_CARD_DEBIT_CREDIT"
    BANK_CATEGORY = "BANKCATEGORY"
    BANK_COUNTRY = "BANKCOUNTRY"
    BANK_NO_MEMBERSHIP = "BANKNOMEMBERSHIP"
    BATCH_DURATION = "BATCHDURATION"
    BATCH_RECLOSE_GUID = "BATCHRECLOSEGUID"
    BATCH_TIME_OFFSET = "BATCHTIMEOFFSET"
    BATCH_UPLOAD = "BATCHUPLOAD"
    BILLING_ADDRESS = "BILLINGADDRESS"
    BILLING_CITY = "BILLINGCITY"
    BILLING_COUNTRY = "BILLINGCOUNTRY"
    BILLING_STATE = "BILLINGSTATE"
    BILLING_TYPE = "BILLINGTYPE"
    BILLING_ZIPCODE = "BILLINGZIPCODE"
    BIN_ACCOUNT_EXCLUSIONS = "BINAccountExclusions"
    BIN_ROUTING_INDEX = "BINRoutingIndex"
    BIN_ROUTING_LIST = "BINRoutingList"
    BROWSER_ACCEPT_HEADER = "BROWSERACCEPTHEADER"
    BROWSER_COLOR_DEPTH = "BROWSERCOLORDEPTH"
    BROWSER_JAVA_ENABLED = "BROWSERJAVAENABLED"
    BROWSER_LANGUAGE = "BROWSERLANGUAGE"
    BROWSER_SCREEN_HEIGHT = "BROWSERSCREENHEIGHT"
    BROWSER_SCREEN_WIDTH = "BROWSERSCREENWIDTH"
    BROWSER_TIME_ZONE = "BROWSERTIMEZONE"
    BROWSER_USER_AGENT = "BROWSERUSERAGENT"
    CAPTURE_DAYS = "CAPTUREDAYS"
    CARDINAL_API_IDENTIFIER = "CARDINAL_API_IDENTIFIER"
    CARDINAL_API_KEY = "CARDINAL_API_KEY"
    CARDINAL_ORG_UNIT_ID = "CARDINAL_ORG_UNIT_ID"
    CARDINAL_SUB_PID = "CARDINAL_SUB_PID"
    CARDNO = "CARDNO"
    CARD_HASH = "CARDHASH"
    CASCADE_ACCOUNT_LIST = "CASCADEACCOUNTLIST"
    CASCADE_BANK_CODES = "CASCADEBANKCODES"
    CASCADE_DISABLED = "CASCADEDISABLED"
    CASCADE_ERROR_CODES = "CASCADEERRORCODES"
    CASCADE_LAST_PROCESSOR = "CASCADELASTPROCESSOR"
    CASCADE_RETRY_TYPE = "CASCADERETRYTYPE"
    CASCADE_TRIED_LIST = "CASCADETRIEDLIST"
    CLONE_CUSTOMER_RECORD = "CLONECUSTOMERRECORD"
    CLONE_TO_CUSTOMER_ID = "CLONETOCUSTOMERID"
    COF_FRAMEWORK = "COFFRAMEWORK"
    CURRENCY = "CURRENCY"
    CUSTOMER_CREATED_DATE = "customerCreatedDate"
    CUSTOMER_FIRSTNAME = "CUSTOMERFIRSTNAME"
    CUSTOMER_LASTNAME = "CUSTOMERLASTNAME"
    CUSTOMER_PASSWORD = "CUSTOMERPASSWORD"
    CUSTOMER_PHONE_NO = "CUSTOMERPHONENO"
    CUSTOMER_VELOCITY = "customerVelocity"
    CUSTOMER_VELOCITY_CURRENCY = "customerVelocityCurrency"
    CVV2 = "CVV2"
    CVV2_CHECK = "CVV2CHECK"
    CVV_OVERRIDES_FOREIGN_AVS = "CVVOverridesForeignAVS"
    DO_NOT_SEND_INCOMPLETE_3DS_AUTHENTICATION = "DO_NOT_SEND_INCOMPLETE_3DS_AUTH"
    DO_NOT_SEND_VOIDS = "doNotSendVoids"
    EMAIL = "EMAIL"
    EMBEDDED_FIELDS_TOKEN = "embeddedFieldsToken"
    ENABLE_3DS_PREPAID = "enable3DSPrepaid"
    EXISTING_CREDITS = "EXISTINGCREDITS"
    EXPIRATION_RETRIES = "expirationRetries"
    EXPIRE_MONTH = "EXPIREMONTH"
    EXPIRE_YEAR = "EXPIREYEAR"
    FAILED_GUID = "FAILEDGUID"
    FAILED_REASON_CODE = "FAILEDREASONCODE"
    FAILED_RESPONSE_CODE = "FAILEDRESPONSECODE"
    FAILED_SERVER = "FAILEDSERVER"
    FAILURE_URL = "FAILUREURL"
    FILENAME = "FILENAME"
    FORCED_CARD_TYPE = "FORCED_CARD_TYPE"
    GATEWAY_CONNECT_TIMEOUT = "gatewayConnectTimeout"
    GATEWAY_PORTNO = "gatewayPortNo"
    GATEWAY_READ_TIMEOUT = "gatewayReadTimeout"
    GATEWAY_SERVER = "gatewayServer"
    GATEWAY_SERVLET = "gatewayServlet"
    GATEWAY_URL = "gatewayURL"
    GENERATE_POSTBACK = "GENERATEPOSTBACK"
    GOOGLE_PAY_TOKEN = "GOOGLEPAYTOKEN"
    IOVATION_BLACK_BOX = "IOVATIONBLACKBOX"
    IOVATION_DEVICE = "IOVATIONDEVICE"
    IOVATION_RESULTS = "IOVATIONRESULTS"
    IOVATION_RULE = "IOVATIONRULE"
    IOVATION_RULE_COUNT = "IOVATIONRULECOUNT"
    IOVATION_RULE_REASON_ = "IOVATIONRULEREASON_"
    IOVATION_RULE_SCORE_ = "IOVATIONRULESCORE_"
    IOVATION_RULE_TYPE_ = "IOVATIONRULETYPE_"
    IOVATION_SCORE = "IOVATIONSCORE"
    IOVATION_TRACKING_NO = "IOVATIONTRACKINGNO"
    IP2LOCATION_COUNTRY = "IP2LOCATIONCOUNTRY"
    IP2LOCATION_USAGE_TYPE = "IP2LOCATIONUSAGETYPE"
    IPADDRESS = "IPADDRESS"
    IS_3DSECURE_AUTHREQ = "is3DSecureAuthReq"
    IS_3DSECURE_BYPASS = "is3DSecureBypass"
    IS_3DSECURE_FRICTIONLESS = "IS_3DSECURE_FRICTIONLESS"
    IS_3DSECURE_INELIGIBLE = "is3DSecureIneligible"
    IS_3DSECURE_NOT_ENROLLED = "is3DSecureNotEnrolled"
    IS_3DS_LOOKUP_RETRY = "is3DSLookupRetry"
    LANGUAGE = "LANGUAGE"
    MAX_CASCADE_ATTEMPTS = "MAXCASCADEATTEMPTS"
    MERCHANT_ACCOUNT = "MERCHANTACCOUNT"
    MERCHANT_ACCOUNT_INDEX = "MERCHANTACCOUNTINDEX"
    MERCHANT_CASCADED_AUTH = "MERCHANTCASCADEDAUTH"
    MERCHANT_CUSTOMER_ID = "MERCHANTCUSTOMERID"
    MERCHANT_DESCRIPTOR = "MERCHANTDESCRIPTOR"
    MERCHANT_DESCRIPTOR_CITY = "MERCHANTDESCRIPTORCITY"
    MERCHANT_DESCRIPTOR_SET = "MERCHANTDESCRIPTORSET"
    MERCHANT_DESCRIPTOR_TRIAL = "MERCHANTDESCRIPTORTRIAL"
    MERCHANT_DESCRIPTOR_TRIAL_SET = "MERCHANTDESCRIPTORTRIALSET"
    MERCHANT_ID = "MERCHANTID"
    MERCHANT_INVOICE_ID = "MERCHANTINVOICEID"
    MERCHANT_PASSWORD = "MERCHANTPASSWORD"
    MERCHANT_PRODUCT_ID = "MERCHANTPRODUCTID"
    MERCHANT_SITE_ID = "MERCHANTSITEID"
    NETWORK_CRYPTOGRAM = "NETWORKCRYPTOGRAM"
    NETWORK_CRYPTOGRAM_ECI = "NETWORKCRYPTOGRAMECI"
    NETWORK_MERCHANT_ENTITY_ID = "networkMerchantEntityID"
    NETWORK_TOKEN = "NETWORKTOKEN"
    NETWORK_TOKENIZATION_DISABELD = "NETWORKTOKENIZATIONDISABELD"
    NETWORK_TOKEN_EXPIRY_MONTH = "NETWORKTOKENEXPIRYMONTH"
    NETWORK_TOKEN_EXPIRY_YEAR = "NETWORKTOKENEXPIRYYEAR"
    NETWORK_TOKEN_EXTERNAL_ID = "networkTokenExternalID"
    NETWORK_TOKEN_GUID = "networkTokenGuid"
    NETWORK_TOKEN_REQUESTOR_ID = "NETWORKTOKENREQUESTORID"
    NON_RELOADABLE_PREPAID_CARD = "NON_RELOADABLE_PREPAID_CARD"
    OMIT_RECEIPT = "OMITRECEIPT"
    ONCLICK_LOGO_URL = "onClickLogoURL"
    ONE_DOLLAR_FALLBACK_FOR_ZERO_DOLLAR_AUTH = "ONE_DOLLAR_FALLBACK_FOR_ZERO_DOLLAR_AUTH"
    OPERATION_TYPE = "OPERATION"
    ORIGINAL_EXPIRE_MONTH = "originalExpireMonth"
    ORIGINAL_EXPIRE_YEAR = "originalExpireYear"
    PARES = "PARES"
    PARTIAL_AUTH_FLAG = "PARTIALAUTHFLAG"
    PAYINFO_TRANSACT_ID= "PAYINFOTRANSACTID"
    PAYMENT_LINK_TOKEN = "PAYMENTLINKTOKEN"
    PAY_HASH = "cardHash"
    POSTING_IPADDRESS = "POSTINGIPADDRESS"
    PREFERRED_MERCHANT_ACCOUNT = "PREFERREDMERCHANTACCOUNT"
    PROCESSOR_3DS = "PROCESSOR3DS"
    REBILL_AMOUNT = "REBILLAMOUNT"
    REBILL_AMOUNT_ON_3DS_LOOKUP = "REBILLAMOUNTON3DSLOOKUP"
    REBILL_COUNT = "REBILLCOUNT"
    REBILL_END_DATE = "REBILLENDDATE"
    REBILL_FEE = "REBILLFEE"
    REBILL_FLAG = "REBILLFLAG"
    REBILL_FREQUENCY = "REBILLFREQUENCY"
    REBILL_REACTIVATE = "REBILLREACTIVATE"
    REBILL_RESUME = "REBILLRESUME"
    REBILL_START = "REBILLSTART"
    REBILL_SUSPEND = "REBILLSUSPEND"
    REBILL_TRANS_NUMBER = "REBILLTRANSNUMBER"
    REFERENCE_GUID = "REFERENCEGUID"
    REFERENCE_SCHEME_SETTLEMENT_DATE = "SCHEMESETTLEDATE"
    REFERENCE_SCHEME_TRANSACTION_ID = "SCHEMETRANID"
    REFERRAL_NO = "REFERRALNO"
    REFERRED_CUSTOMER_ID = "REFERREDCUSTOMERID"
    REFERRER_ALLOW_OVERRIDE_FLAG = "REFERRERALLOWOVERRIDEFLAG"
    REFERRER_PASSWORD = "REFERRERPASSWORD"
    REFERRER_SUBMIT_FLAG = "REFERRERSUBMITFLAG"
    REFERRER_URL = "REFERRERURL"
    REFERRING_MERCHANT_ID = "REFERRINGMERCHANTID"
    RETRY_3DSECURE_DECLINES = "retry3DSecureDeclines"
    RETRY_3DSECURE_FAILED_AUTHENTICATION = "retry3DSecureFailedAuthentication"
    RETRY_OMIT_CASCADE_ACCOUNTS = "RETRYOMITACCOUNTS"
    ROUTING_NO = "routingNo"
    SAVINGS_ACCOUNT = "savingsAccount"
    SCRUB = "SCRUB"
    SCRUB_ACTIVITY = "SCRUBACTIVITY"
    SCRUB_NEGDB = "SCRUBNEGDB"
    SCRUB_PROFILE = "SCRUBPROFILE"
    SEND_MC_AUTH_INDICATOR = "SEND_MC_AUTH_INDICATOR"
    SHOW_PAYMENT_FORM = "SHOW_PAYMENT_FORM"
    SITE_NO = "SITENO"
    SS_NUMBER = "SSNUMBER"
    STYLE_SHEET = "style"
    STYLE_SHEET2 = "style2"
    STYLE_SHEET3 = "style3"
    SUBMISSION_NUMBER = "SUBMISSIONNUMBER"
    SUBMIT_ZERO_DOLLAR_AS_ONE_DOLLAR = "SUBMITZERODOLLARASONEDOLLAR"
    SUCCESS_URL = "SUCCESSURL"
    TEST_SITE = "TESTSITE"
    THREATMETRIX_SESSION_ID = "THREATMETRIXSESSIONID"
    TRANSACTION_TYPE = "TRANSACTIONTYPE"
    TRANSACT_ID = "referenceGUID"
    TRANSLATIONS = "translations"
    UDF01 = "UDF01"
    UDF02 = "UDF02"
    USERNAME = "USERNAME"
    USE_3D_SECURE = "USE3DSECURE"
    USE_PRIMARY_SCHEMEID = "USEPRIMARYSCHEMEID"
    XSELL_CUSTOMER_ID = "XSELLCUSTOMERID"
    XSELL_FLAG = "XSELLFLAG"
    XSELL_MERCHANT_ACCOUNT = "XSELLMERCHANTACCOUNT"
    XSELL_MERCHANT_ACCOUNT_INDEX = "XSELLMERCHANTACCOUNTINDEX"
    XSELL_MERCHANT_ID = "XSELLMERCHANTID"
    XSELL_ORIGINAL_MERCHANT_CUSTOMER_ID = "XSELLORIGINALMERCHANTCUSTOMERID"
    XSELL_ORIGINAL_MERCHANT_ID = "XSELLORIGINALMERCHANTID"
    XSELL_REFERENCE_XACT = "XSELLREFERENCEXACT"
    _3DSECURE_ACS_TRANSACTION_ID = "_3DSECURE_ACS_TRANSACTION_ID"
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
    _3DSECURE_CHALLENGE_MANDATED_INDICATOR = "_3DSECURE_CHALLENGE_MANDATED_INDICATOR"
    _3DSECURE_DF_REFERENCE_ID = "_3DSECURE_DF_REFERENCE_ID"
    _3DSECURE_DS_TRANSACTION_ID = "_3DSECURE_DS_TRANSACTION_ID"
    _3DSECURE_LOOKUP_CHALLENGE_INDICATOR = "_3DSECURE_LOOKUP_CHALLENGE_INDICATOR"
    _3DSECURE_LOOKUP_SIGNATURE = "_3DSECURE_LOOKUP_SIGNATURE"
    _3DSECURE_REDIRECT_URL = "_3DSECURE_REDIRECT_URL"
    _3DSECURE_THREE_DS_SERVER_TRANSACTION_ID = "_3DSECURE_THREE_DS_SERVER_TRANSACTION_ID"
    _3D_CAVV_ALGORITHM = "THREEDCAVVALGORITHM"
    _3D_CAVV_UCAF = "THREEDCAVVUCAF"
    _3D_CHECK = "THREEDCHECK"
    _3D_ECI = "THREEDECI"
    _3D_PARESSTATUS = "THREEDPARESSTATUS"
    _3D_SIGNATURE = "THREEDSIGNATURE"
    _3D_VERSION = "THREEDVERSION"
    _3D_VERSTATUS = "THREEDVERSTATUS"
    _3D_XID = "THREEDXID"

    def __init__(self):
        """Constructor for class."""

        self.parameterList = {}
        self.Set(GatewayRequest.VERSION_INDICATOR, GatewayRequest.VERSION_NUMBER)

    def Set(self, key, value):
        """Sets a value in the parameter list."""

        self.Clear(key)  # Have key value? Delete it
        self.parameterList[key] = str(value)  # Save the value

    def Clear(self, key):
        """Clears a value in the parameter list."""

        if key in self.parameterList:  # Have key value?
            del self.parameterList[key]  # Delete it

    def Get(self, key):
        """Gets a value from the parameter list."""

        if key in self.parameterList:  # Have key value?
            return self.parameterList[key]  # Return the value
        return None  # Don't have a value

    def ToXML(self):
        """Creates an XML document from the hash list."""

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

    ACS_URL = "acsURL"
    APPROVED_AMOUNT = "approvedAmount"
    APPROVED_CURRENCY = "approvedCurrency"
    AUTH_NO = "authNo"
    AVS_RESPONSE = "avsResponse"
    BALANCE_AMOUNT = "balanceAmount"
    BALANCE_CURRENCY = "balanceCurrency"
    BANK_RESPONSE_CODE = "bankResponseCode"
    BATCH_CREDIT_COUNT = "batchCreditCount"
    BATCH_CREDIT_TOTAL = "batchCreditTotal"
    BATCH_NUMBER = "batchNumber"
    BATCH_SALES_COUNT = "batchSalesCount"
    BATCH_SALES_TOTAL = "batchSalesTotal"
    BILLING_ADDRESS = "billingAddress"
    BILLING_CITY = "billingCity"
    BILLING_COUNTRY = "billingCountry"
    BILLING_STATE = "billingState"
    BILLING_ZIPCODE = "billingZipCode"
    CACHED_3DSECURE_SCRUB = "cached3DSecureScrub"
    CARDHOLDER_REASON_CODE_DESCRIPTION = "cardholderReasonCodeDescription"
    CARD_BIN = "cardBin"
    CARD_COUNTRY = "cardCountry"
    CARD_DEBIT_CREDIT = "cardDebitCredit"
    CARD_DESCRIPTION = "cardDescription"
    CARD_EXPIRATION = "cardExpiration"
    CARD_HASH = "cardHash"
    CARD_ISSUER_NAME = "cardIssuerName"
    CARD_ISSUER_PHONE = "cardIssuerPhone"
    CARD_ISSUER_URL = "cardIssuerURL"
    CARD_REGION = "cardRegion"
    CARD_TYPE = "cardType"
    CAVV_RESPONSE = "cavvResponse"
    CUSTOMER_FIRSTNAME = "customerFirstName"
    CUSTOMER_LASTNAME = "customerLastName"
    CVV2_CODE = "cvv2Code"
    DATA = "data"
    ECI = "ECI"
    EMAIL = "email"
    EXCEPTION = "exception"
    IOVATION_BLACK_BOX = "IOVATIONBLACKBOX"
    IOVATION_DEVICE = "IOVATIONDEVICE"
    IOVATION_ECHO= "IOVATIONECHO"
    IOVATION_RESULTS = "IOVATIONRESULTS"
    IOVATION_RULE_COUNT = "IOVATIONRULECOUNT"
    IOVATION_RULE_REASON_ = "IOVATIONRULEREASON_"
    IOVATION_RULE_SCORE_ = "IOVATIONRULESCORE_"
    IOVATION_RULE_TYPE_ = "IOVATIONRULETYPE_"
    IOVATION_SCORE = "IOVATIONSCORE"
    IOVATION_SURE_SCORE = "IOVATIONSURESCORE"
    IOVATION_TRACKING_NO = "IOVATIONTRACKINGNO"
    IS_BANK_HARD_DECLINE = "isBankHardDecline"
    JOIN_AMOUNT = "joinAmount"
    JOIN_DATE = "joinDate"
    LAST_BILLING_AMOUNT = "lastBillingAmount"
    LAST_BILLING_DATE = "lastBillingDate"
    LAST_REASON_CODE = "lastReasonCode"
    MERCHANT_ACCOUNT = "merchantAccount"
    MERCHANT_ADVICE_CODE = "merchantAdviceCode"
    MERCHANT_CUSTOMER_ID = "merchantCustomerID"
    MERCHANT_INVOICE_ID = "merchantInvoiceID"
    MERCHANT_PRODUCT_ID = "merchantProductID"
    MERCHANT_SITE_ID = "merchantSiteID"
    OPERATION = "operation"
    PAREQ = "PAREQ"
    PARES = "PARES"
    PAYMENT_LINK_URL = "PAYMENT_LINK_URL"
    PAY_LAST_FOUR = "cardLastFour"
    PAY_TYPE = "payType"
    PAY_TYPE_CREDIT = "CREDIT"
    PAY_TYPE_DEBIT = "DEBIT"
    PROCESSOR_3DS = "PROCESSOR3DS"
    REASON_CODE = "reasonCode"
    REASON_CODE_NAME = "reasonCodeName"
    REBILL_AMOUNT = "rebillAmount"
    REBILL_CURRENCY = "rebillCurrency"
    REBILL_DATE = "rebillDate"
    REBILL_END_DATE = "rebillEndDate"
    REBILL_FREQUENCY = "rebillFrequency"
    REBILL_STATUS = "rebillStatus"
    REFERENCE_NO = "referenceNo"
    RESPONSE_CODE = "responseCode"
    RETRIEVAL_ID = "retrievalNo"
    RETURNED_ACI = "returnedACI"
    SCHEME_SETTLEMENT_DATE = "schemeSettlementDate"
    SCHEME_TRANSACTION_ID = "schemeTransactionID"
    SCRUB_RESULTS = "scrubResults"
    SETTLED_AMOUNT = "approvedAmount"
    SETTLED_CURRENCY = "approvedCurrency"
    TRANSACTION_TIME = "transactionTime"
    TRANSACT_ID = "guidNo"
    _3DSECURE_ACS_TRANSACTION_ID = "_3DSECURE_ACS_TRANSACTION_ID"
    _3DSECURE_CAVV_ALGORITHM = "_3DSECURE_CAVV_ALGORITHM"
    _3DSECURE_CAVV_UCAF = "_3DSECURE_CAVV_UCAF"
    _3DSECURE_CHALLENGE_INDICATOR = "_3DSECURE_CHALLENGE_INDICATOR"
    _3DSECURE_CHALLENGE_MANDATED_INDICATOR = "_3DSECURE_CHALLENGE_MANDATED_INDICATOR"
    _3DSECURE_DEVICE_COLLECTION_JWT = "_3DSECURE_DEVICE_COLLECTION_JWT"
    _3DSECURE_DEVICE_COLLECTION_URL = "_3DSECURE_DEVICE_COLLECTION_URL"
    _3DSECURE_DS_TRANSACTION_ID = "_3DSECURE_DS_TRANSACTION_ID"
    _3DSECURE_LOOKUP_CHALLENGE_INDICATOR = "_3DSECURE_LOOKUP_CHALLENGE_INDICATOR"
    _3DSECURE_LOOKUP_REFERENCE_GUID = "_3D_LOOKUP_REFERENCE_GUID"
    _3DSECURE_LOOKUP_SIGNATURE = "_3DSECURE_LOOKUP_SIGNATURE"
    _3DSECURE_PARESSTATUS = "_3DSECURE_PARESSTATUS"
    _3DSECURE_STEP_UP_JWT = "_3DSECURE_STEP_UP_JWT"
    _3DSECURE_STEP_UP_URL = "_3DSECURE_STEP_UP_URL"
    _3DSECURE_THREE_DS_SERVER_TRANSACTION_ID = "_3DSECURE_THREE_DS_SERVER_TRANSACTION_ID"
    _3DSECURE_VERSION = "_3DSECURE_VERSION"
    _3DSECURE_VERSTATUS = "_3DSECURE_VERSTATUS"
    _3DSECURE_XID = "_3DSECURE_XID"

    def __init__(self):
        """Constructor for class."""

        self.parameterList = {}  # Fresh list
        self.haveOpenTag = 0  # Haven't seen <gatewayResponse>
        self.valueBuffer = ""  # No value yet

    def Set(self, key, value):
        """Sets a value in the parameter list."""

        if key in self.parameterList:  # Have key value?
            del self.parameterList[key]  # Delete it
        self.parameterList[key] = str(value)  # Save the value

    def Reset(self):
        """Clears all elements in a response."""

        del self.parameterList  # Kill old list
        self.parameterList = {}  # Start with fresh list

    def Get(self, key):
        """Gets a value from the parameter list."""

        if key in self.parameterList:  # Have key value?
            return self.parameterList[key]  # Return the value
        return None  # Don't have a value

    def SetFromXML(self, xmlDocument):
        """Sets values in a response object using an XML document."""

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

    def startElement(self, name, attrs):
        """Handler for start of XML element."""

        if name == "gatewayResponse":  # Opening of document?
            self.haveOpenTag = 1  # Have seen open tag
        self.valueBuffer = ""  # Start with clean value

    def characters(self, data):
        """Handler for element string"""

        if self.haveOpenTag:  # Seen open yet?
            self.valueBuffer += data

    def endElement(self, name):
        """Handler for end of XML element."""

        if name != "gatewayResponse":  # Opening of document?
            self.Set(name, self.valueBuffer)


class GatewayService:
    ######################################################################
    #
    #	Define constants
    #
    ######################################################################

    ROCKETGATE_SERVLET = "/gateway/servlet/ServiceDispatcherAccess"
    ROCKETGATE_CONNECT_TIMEOUT = 10
    ROCKETGATE_READ_TIMEOUT = 90
    ROCKETGATE_PORTNO = 443
    ROCKETGATE_USER_AGENT = "RG Client - Python " + str(GatewayRequest.VERSION_NUMBER)

    LIVE_HOST = "gateway.rocketgate.com"
    LIVE_HOST_16 = "gateway-16.rocketgate.com"
    LIVE_HOST_17 = "gateway-17.rocketgate.com"
    TEST_HOST = "dev-gateway.rocketgate.com"

    def __init__(self):
        """Constructor for class."""

        self.testMode = 0  # Default to live
        self.rocketGateHost = GatewayService.LIVE_HOST
        self.rocketGateServlet = GatewayService.ROCKETGATE_SERVLET
        self.rocketGatePortNo = GatewayService.ROCKETGATE_PORTNO
        self.rocketGateConnectTimeout = GatewayService.ROCKETGATE_CONNECT_TIMEOUT
        self.rocketGateReadTimeout = GatewayService.ROCKETGATE_READ_TIMEOUT

    def SetTestMode(self, yesNo):
        """Selects test/development mode."""

        if yesNo:  # Setting test mode?
            self.testMode = 1  # Set to test mode
            del self.rocketGateHost  # Delete old host list
            self.rocketGateHost = GatewayService.TEST_HOST
        else:
            self.testMode = 0  # Set to live mode
            del self.rocketGateHost  # Delete old host list
            self.rocketGateHost = GatewayService.LIVE_HOST

    def SetHost(self, hostName):
        """Sets the host used by the service"""

        del self.rocketGateHost  # Delete old host list
        self.rocketGateHost = hostName  # Use this host

    def SetPortNo(self, portNo):
        """Sets the port number used by the service."""

        try:
            value = int(portNo)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGatePortNo = value
        except:
            pass

    def SetServlet(self, servlet):
        """Sets servlet used by the service."""

        self.rocketGateServlet = servlet  # End point

    def SetConnectTimeout(self, timeout):
        """Sets connection timeout"""

        try:
            value = int(timeout)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGateConnectTimeout = value
        except:
            pass

    def SetReadTimeout(self, timeout):
        """Sets read timeout"""

        try:
            value = int(timeout)  # Get numeric value
            if value > 0:  # Have a valid value?
                self.rocketGateReadTimeout = value
        except:
            pass

    def SendTransaction(self, serverName, request, response):
        """Sends a transaction to a named host."""

        #
        #	Gather overrides for transaction.
        #
        connection = None
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
        headers = {"Content-Type": "text/xml", "User-Agent": GatewayService.ROCKETGATE_USER_AGENT}

        #
        #	Create the HTTP handler and post our request.
        #
        try:
            connection = http.client.HTTPSConnection(serverName, urlPortNo, timeout=connectTimeout)
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
                response.Set(GatewayResponse.EXCEPTION,  str(results.status) + ": " + body)
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
            if connection is not None:
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

    def PerformTransaction(self, request, response):
        """Performs the transaction described in a gateway request."""

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
            request.Set(GatewayRequest.FAILED_RESPONSE_CODE,  response.Get(GatewayResponse.RESPONSE_CODE))
            request.Set(GatewayRequest.FAILED_REASON_CODE,  response.Get(GatewayResponse.REASON_CODE))
            request.Set(GatewayRequest.FAILED_GUID,  response.Get(GatewayResponse.TRANSACT_ID))
            index += 1  # Next index

        #
        #	If we ran out of places to send this, just quit.
        #
        return 0  # Must quit

    def PerformTargetedTransaction(self, request, response):
        """Sends a transaction to a server based upon the GUID."""

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
        if referenceGUID is None:  # Don't have reference?
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
            server_name = self.rocketGateHost  # Start with default
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

    def PerformConfirmation(self, request, response):
        """Performs the confirmation pass that tells the server we have received the transaction reply."""

        #
        #	Verify that we have a transaction ID for the
        #	confirmation message.
        #
        confirmGUID = response.Get(GatewayResponse.TRANSACT_ID)
        if confirmGUID == None:  # Don't have reference?
            response.Set(GatewayResponse.EXCEPTION, "BUG-CHECK - Missing confirmation GUID")
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
        response.Set(GatewayResponse.RESPONSE_CODE, confirmResponse.Get(GatewayResponse.RESPONSE_CODE))
        response.Set(GatewayResponse.REASON_CODE, confirmResponse.Get(GatewayResponse.REASON_CODE))
        return 0  # And quit

    def PerformAuthOnly(self, request, response):
        """Performs an auth-only transaction."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_AUTH")
        results = self.PerformTransaction(request, response)
        if results:  # Success?
            results = self.PerformConfirmation(request, response)
        return results  # Return results

    def PerformTicket(self, request, response):
        """Performs a Ticket operation for a previous auth-only transaction."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_TICKET")
        results = self.PerformTargetedTransaction(request, response)
        return results  # Return results

    def PerformPurchase(self, request, response):
        """Performs a complete purchase transaction."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_PURCHASE")
        results = self.PerformTransaction(request, response)
        if results:  # Success?
            results = self.PerformConfirmation(request, response)
        return results  # Return results

    def PerformCredit(self, request, response):
        """Performs a Credit operation for a previous transaction."""

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

    def PerformVoid(self, request, response):
        """Performs a Void operation for a previous transaction."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CC_VOID")
        results = self.PerformTargetedTransaction(request, response)
        return results  # Return results

    def PerformCardScrub(self, request, response):
        """Performs scrubbing on a card/customer"""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CARDSCRUB")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    def PerformRebillCancel(self, request, response):
        """Schedules cancellation of rebilling."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "REBILL_CANCEL")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    def PerformRebillUpdate(self, request, response):
        """Updates terms of a rebilling."""

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

    def PerformCardUpload(self, request, response):
        """Uploads card data to the servers."""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "CARDUPLOAD")
        results = self.PerformTransaction(request, response)
        return results  # Return results

    def PerformLookup(self, request, response):
        """Performs GUID lookup"""

        request.Set(GatewayRequest.TRANSACTION_TYPE, "LOOKUP")
        referenceGUID = request.Get(GatewayRequest.REFERENCE_GUID)
        if referenceGUID is not None:  # Have reference?
            results = self.PerformTargetedTransaction(request, response)
        else:
            results = self.PerformTransaction(request, response)
        return results

    def GenerateXsell(self, request, response):
        """Adds an entry to the XsellQueue."""

        # Apply the transaction type to the request
        request.Set(GatewayRequest.TRANSACTION_TYPE, "GENERATEXSELL")
        request.Set(GatewayRequest.REFERENCE_GUID, request.Get(GatewayRequest.XSELL_REFERENCE_XACT))

        if request.Get(GatewayRequest.REFERENCE_GUID) is not None:
            return self.PerformTargetedTransaction(request, response)
        else:
            return self.PerformTransaction(request, response)

    def BuildPaymentLink(self, request, response) -> bool:
        """Creates an embeddable RocketGate hosted payment link"""

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
    REASON_INVALID_CPF_FORMAT = 463
    REASON_INVALID_GOOGLE_PAY_TOKEN = 464
