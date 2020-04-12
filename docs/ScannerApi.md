# ib_web_api.ScannerApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_scanner_params_get**](ScannerApi.md#iserver_scanner_params_get) | **GET** /iserver/scanner/params | get lists of available scanners
[**iserver_scanner_run_post**](ScannerApi.md#iserver_scanner_run_post) | **POST** /iserver/scanner/run | run scanner to get a list of contracts


# **iserver_scanner_params_get**
> InlineResponse2009 iserver_scanner_params_get()

get lists of available scanners

Returns an object contains four lists contain all parameters for scanners

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ScannerApi()

try:
    # get lists of available scanners
    api_response = api_instance.iserver_scanner_params_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->iserver_scanner_params_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_scanner_run_post**
> list[InlineResponse20010] iserver_scanner_run_post(body)

run scanner to get a list of contracts

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ScannerApi()
body = ib_web_api.ScannerParams() # ScannerParams | modify-order request

try:
    # run scanner to get a list of contracts
    api_response = api_instance.iserver_scanner_run_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannerApi->iserver_scanner_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScannerParams**](ScannerParams.md)| modify-order request | 

### Return type

[**list[InlineResponse20010]**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

