import requests
from pprint import pprint

def introspection_info(obj):
    result_dict = {}
    result_dict.update({'type': type(obj)})
    result_dict.update({'attrs': [method for method in dir(obj) if not callable(getattr(obj, method)) and not method.startswith("__")]})
    result_dict.update(
        {'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]})
    result_dict.update({'module': getattr(obj, "__module__", "No module info")})
    if isinstance(obj, (int, float, complex)):
        result_dict['is_numeric'] = True
    elif isinstance(obj, str):
        result_dict['is_string'] = True
    elif isinstance(obj, list):
        result_dict['is_list'] = True
        result_dict['length'] = len(obj)
    elif isinstance(obj, dict):
        result_dict['is_dict'] = True
        result_dict['keys'] = list(obj.keys())
    elif isinstance(obj, (set, frozenset)):
        result_dict['is_set'] = True
    pprint(result_dict)

introspection_info(requests)
introspection_info('6654')