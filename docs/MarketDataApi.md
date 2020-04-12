# ib_web_api.MarketDataApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_marketdata_history_get**](MarketDataApi.md#iserver_marketdata_history_get) | **GET** /iserver/marketdata/history | Market Data History
[**iserver_marketdata_snapshot_get**](MarketDataApi.md#iserver_marketdata_snapshot_get) | **GET** /iserver/marketdata/snapshot | Market Data


# **iserver_marketdata_history_get**
> HistoryData iserver_marketdata_history_get(conid, period, bar=bar)

Market Data History

Get history of market Data for the given conid, length of data is controlled by period and bar. e.g. 1y period with bar =1w returns 52 data points

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.MarketDataApi()
conid = 'conid_example' # str | contract id
period = 'period_example' # str | time period-- 1d,1w,1m,1y
bar = 'bar_example' # str | possible value-- 5min,1h,1w (optional)

try:
    # Market Data History
    api_response = api_instance.iserver_marketdata_history_get(conid, period, bar=bar)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 
 **period** | **str**| time period-- 1d,1w,1m,1y | 
 **bar** | **str**| possible value-- 5min,1h,1w | [optional] 

### Return type

[**HistoryData**](HistoryData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_marketdata_snapshot_get**
> list[InlineResponse2007] iserver_marketdata_snapshot_get(conids, since=since, fields=fields)

Market Data

Get Market Data for the given conid(s). The end-point will return by default bid, ask, last, change, change pct, close, listing exchange. See response fields for a list of available fields that can be request via fields argument. The endpoint /iserver/accounts should be called prior to /iserver/marketdata/snapshot. To receive all available fields the /snapshot endpoint will need to be called several times. 

### Example
```python
from __future__ import print_function
import time
import ib_web_api
from ib_web_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ib_web_api.MarketDataApi()
conids = 'conids_example' # str | list of conids separated by comma
since = 56 # int | time period since which updates are required. uses epoch time with milliseconds. (optional)
fields = 'fields_example' # str | list of fields separated by comma (optional)

try:
    # Market Data
    api_response = api_instance.iserver_marketdata_snapshot_get(conids, since=since, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketDataApi->iserver_marketdata_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conids** | **str**| list of conids separated by comma | 
 **since** | **int**| time period since which updates are required. uses epoch time with milliseconds. | [optional] 
 **fields** | **str**| list of fields separated by comma | [optional] 

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

