# ib_web_api.OrderApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_account_account_id_order_orig_customer_order_id_delete**](OrderApi.md#iserver_account_account_id_order_orig_customer_order_id_delete) | **DELETE** /iserver/account/{accountId}/order/{origCustomerOrderId} | Delete Order
[**iserver_account_account_id_order_orig_customer_order_id_post**](OrderApi.md#iserver_account_account_id_order_orig_customer_order_id_post) | **POST** /iserver/account/{accountId}/order/{origCustomerOrderId} | Modify Order
[**iserver_account_account_id_order_post**](OrderApi.md#iserver_account_account_id_order_post) | **POST** /iserver/account/{accountId}/order | Place Order
[**iserver_account_account_id_order_whatif_post**](OrderApi.md#iserver_account_account_id_order_whatif_post) | **POST** /iserver/account/{accountId}/order/whatif | Preview Order
[**iserver_account_account_id_orders_post**](OrderApi.md#iserver_account_account_id_orders_post) | **POST** /iserver/account/{accountId}/orders | Place Orders (Support bracket orders)
[**iserver_account_orders_get**](OrderApi.md#iserver_account_orders_get) | **GET** /iserver/account/orders | Live Orders
[**iserver_reply_replyid_post**](OrderApi.md#iserver_reply_replyid_post) | **POST** /iserver/reply/{replyid} | Place Order Reply


# **iserver_account_account_id_order_orig_customer_order_id_delete**
> list[InlineResponse2006] iserver_account_account_id_order_orig_customer_order_id_delete(account_id, orig_customer_order_id)

Delete Order

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
account_id = 'account_id_example' # str | account id
orig_customer_order_id = 'orig_customer_order_id_example' # str | Customer OrderId

try:
    # Delete Order
    api_response = api_instance.iserver_account_account_id_order_orig_customer_order_id_delete(account_id, orig_customer_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_orig_customer_order_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **orig_customer_order_id** | **str**| Customer OrderId | 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_orig_customer_order_id_post**
> list[InlineResponse2006] iserver_account_account_id_order_orig_customer_order_id_post(account_id, orig_customer_order_id, body)

Modify Order

Modifies an open order. The /iserver/accounts endpoint must first be called.

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
account_id = 'account_id_example' # str | account id
orig_customer_order_id = 'orig_customer_order_id_example' # str | Customer OrderId
body = ib_web_api.ModifyOrder() # ModifyOrder | modify-order request

try:
    # Modify Order
    api_response = api_instance.iserver_account_account_id_order_orig_customer_order_id_post(account_id, orig_customer_order_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_orig_customer_order_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **orig_customer_order_id** | **str**| Customer OrderId | 
 **body** | [**ModifyOrder**](ModifyOrder.md)| modify-order request | 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_post**
> list[InlineResponse2003] iserver_account_account_id_order_post(account_id, body)

Place Order

Please note here, sometimes this end-point alone can't make sure you submit the order successfully, you could receive some questions in the response, you have to to answer them in order to submit the order successfully. You can use \"/iserver/reply/{replyid}\" end-point to answer questions 

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
account_id = 'account_id_example' # str | account id
body = ib_web_api.OrderRequest() # OrderRequest | order request info

try:
    # Place Order
    api_response = api_instance.iserver_account_account_id_order_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**OrderRequest**](OrderRequest.md)| order request info | 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_whatif_post**
> InlineResponse2005 iserver_account_account_id_order_whatif_post(account_id, body)

Preview Order

This end-point allows you to preview order without actually submitting the order and you can get commission information in the response. 

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
account_id = 'account_id_example' # str | account id
body = ib_web_api.OrderRequest() # OrderRequest | order info

try:
    # Preview Order
    api_response = api_instance.iserver_account_account_id_order_whatif_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_whatif_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**OrderRequest**](OrderRequest.md)| order info | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_orders_post**
> list[InlineResponse2003] iserver_account_account_id_orders_post(account_id, body)

Place Orders (Support bracket orders)

You can pass a list of orders here 

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
account_id = 'account_id_example' # str | account id
body = ib_web_api.Body() # Body | order request info

try:
    # Place Orders (Support bracket orders)
    api_response = api_instance.iserver_account_account_id_orders_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_orders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**Body**](Body.md)| order request info | 

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_orders_get**
> InlineResponse2002 iserver_account_orders_get()

Live Orders

The end-point is meant to be used in polling mode, e.g. requesting every x seconds. The response will contain two objects, one is notification, the other is orders.  Orders is the list of orders (cancelled, filled, submitted) with activity in the current day.  Notifications contains information about execute orders as they happen, see status field. 

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()

try:
    # Live Orders
    api_response = api_instance.iserver_account_orders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_orders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_reply_replyid_post**
> list[InlineResponse2004] iserver_reply_replyid_post(replyid, body)

Place Order Reply

Reply to questions when placing orders and submit orders

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.OrderApi()
replyid = 'replyid_example' # str | Please use the \"id\" from the response of \"Place Order\" end-point
body = ib_web_api.Body1() # Body1 | Answer to question

try:
    # Place Order Reply
    api_response = api_instance.iserver_reply_replyid_post(replyid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_reply_replyid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replyid** | **str**| Please use the \&quot;id\&quot; from the response of \&quot;Place Order\&quot; end-point | 
 **body** | [**Body1**](Body1.md)| Answer to question | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

