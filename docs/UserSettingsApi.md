# launchdarkly_api.UserSettingsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expiring_user_targets_for_user**](UserSettingsApi.md#get_expiring_user_targets_for_user) | **GET** /users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Get expiring dates on flags for user
[**get_user_flag_setting**](UserSettingsApi.md#get_user_flag_setting) | **GET** /users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Fetch a single flag setting for a user by key.
[**get_user_flag_settings**](UserSettingsApi.md#get_user_flag_settings) | **GET** /users/{projectKey}/{environmentKey}/{userKey}/flags | Fetch a single flag setting for a user by key.
[**patch_expiring_user_targets_for_flags**](UserSettingsApi.md#patch_expiring_user_targets_for_flags) | **PATCH** /users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Update, add, or delete expiring user targets for a single user on all flags
[**put_flag_setting**](UserSettingsApi.md#put_flag_setting) | **PUT** /users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Specifically enable or disable a feature flag for a user based on their key.


# **get_expiring_user_targets_for_user**
> UserTargetingExpirationOnFlagsForUser get_expiring_user_targets_for_user(project_key, environment_key, user_key)

Get expiring dates on flags for user

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UserSettingsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
user_key = 'user_key_example' # str | The user's key.

try:
    # Get expiring dates on flags for user
    api_response = api_instance.get_expiring_user_targets_for_user(project_key, environment_key, user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_expiring_user_targets_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **user_key** | **str**| The user&#39;s key. | 

### Return type

[**UserTargetingExpirationOnFlagsForUser**](UserTargetingExpirationOnFlagsForUser.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_flag_setting**
> UserFlagSetting get_user_flag_setting(project_key, environment_key, user_key, feature_flag_key)

Fetch a single flag setting for a user by key.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UserSettingsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
user_key = 'user_key_example' # str | The user's key.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Fetch a single flag setting for a user by key.
    api_response = api_instance.get_user_flag_setting(project_key, environment_key, user_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_user_flag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **user_key** | **str**| The user&#39;s key. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**UserFlagSetting**](UserFlagSetting.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_flag_settings**
> UserFlagSettings get_user_flag_settings(project_key, environment_key, user_key)

Fetch a single flag setting for a user by key.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UserSettingsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
user_key = 'user_key_example' # str | The user's key.

try:
    # Fetch a single flag setting for a user by key.
    api_response = api_instance.get_user_flag_settings(project_key, environment_key, user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->get_user_flag_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **user_key** | **str**| The user&#39;s key. | 

### Return type

[**UserFlagSettings**](UserFlagSettings.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_user_targets_for_flags**
> UserTargetingExpirationOnFlagsForUser patch_expiring_user_targets_for_flags(project_key, environment_key, user_key, semantic_patch_with_comment)

Update, add, or delete expiring user targets for a single user on all flags

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UserSettingsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
user_key = 'user_key_example' # str | The user's key.
semantic_patch_with_comment = NULL # object | Requires a Semantic Patch representation of the desired changes to the resource. 'https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches'. The addition of comments is also supported.

try:
    # Update, add, or delete expiring user targets for a single user on all flags
    api_response = api_instance.patch_expiring_user_targets_for_flags(project_key, environment_key, user_key, semantic_patch_with_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->patch_expiring_user_targets_for_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **user_key** | **str**| The user&#39;s key. | 
 **semantic_patch_with_comment** | **object**| Requires a Semantic Patch representation of the desired changes to the resource. &#39;https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches&#39;. The addition of comments is also supported. | 

### Return type

[**UserTargetingExpirationOnFlagsForUser**](UserTargetingExpirationOnFlagsForUser.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_flag_setting**
> put_flag_setting(project_key, environment_key, user_key, feature_flag_key, user_settings_body)

Specifically enable or disable a feature flag for a user based on their key.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UserSettingsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
user_key = 'user_key_example' # str | The user's key.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
user_settings_body = launchdarkly_api.UserSettingsBody() # UserSettingsBody | 

try:
    # Specifically enable or disable a feature flag for a user based on their key.
    api_instance.put_flag_setting(project_key, environment_key, user_key, feature_flag_key, user_settings_body)
except ApiException as e:
    print("Exception when calling UserSettingsApi->put_flag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **user_key** | **str**| The user&#39;s key. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **user_settings_body** | [**UserSettingsBody**](UserSettingsBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

