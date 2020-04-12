# ib_web_api.ContractApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_contract_conid_info_get**](ContractApi.md#iserver_contract_conid_info_get) | **GET** /iserver/contract/{conid}/info | Contract Info
[**iserver_secdef_search_post**](ContractApi.md#iserver_secdef_search_post) | **POST** /iserver/secdef/search | Search by symbol or name
[**trsrv_futures_get**](ContractApi.md#trsrv_futures_get) | **GET** /trsrv/futures | Security Futures by Symbol
[**trsrv_secdef_post**](ContractApi.md#trsrv_secdef_post) | **POST** /trsrv/secdef | Secdef by Conid


# **iserver_contract_conid_info_get**
> Contract iserver_contract_conid_info_get(conid)

Contract Info

get contract details, you can use this to prefill your order before you submit an order

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ContractApi()
conid = 'conid_example' # str | contract id

try:
    # Contract Info
    api_response = api_instance.iserver_contract_conid_info_get(conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_contract_conid_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_search_post**
> list[InlineResponse2008] iserver_secdef_search_post(symbol)

Search by symbol or name

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ContractApi()
symbol = ib_web_api.Symbol() # Symbol | symbol or name to be searched

try:
    # Search by symbol or name
    api_response = api_instance.iserver_secdef_search_post(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | [**Symbol**](Symbol.md)| symbol or name to be searched | 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_futures_get**
> InlineResponse20016 trsrv_futures_get(symbols)

Security Futures by Symbol

Returns a list of non-expired future contracts for given symbol(s)

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ContractApi()
symbols = 'symbols_example' # str | list of case-sensitive symbols separated by comma

try:
    # Security Futures by Symbol
    api_response = api_instance.trsrv_futures_get(symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_futures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| list of case-sensitive symbols separated by comma | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_secdef_post**
> Secdef trsrv_secdef_post(body)

Secdef by Conid

Returns a list of security definitions for the given conids

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.ContractApi()
body = ib_web_api.Body5() # Body5 | request body

try:
    # Secdef by Conid
    api_response = api_instance.trsrv_secdef_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_secdef_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)| request body | 

### Return type

[**Secdef**](Secdef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

