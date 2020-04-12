# HistoryData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | start date time | [optional] 
**md_availability** | **str** | Market Data Availability. The field may contain two chars. The first char is the primary code: R &#x3D; Realtime, D &#x3D; Delayed, Z &#x3D; Frozen, Y &#x3D; Frozen Delayed. The second char is the secondary code: P &#x3D; Snapshot Available, p &#x3D; Consolidated.  | [optional] 
**bar_length** | **int** |  | [optional] 
**delay** | **int** |  | [optional] 
**high** | **str** | price/volume/... | [optional] 
**low** | **str** | price/volume/... | [optional] 
**symbol** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**tick_num** | **str** |  | [optional] 
**time_period** | **str** |  | [optional] 
**data** | [**list[HistorydataData]**](HistorydataData.md) |  | [optional] 
**points** | **float** | total number of points | [optional] 
**travel_time** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


