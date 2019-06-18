import json

DEFAULT_HEADER = {}
DEFAULT_METHOD = "POST"
DEFAULT_BODY = ""
DEFAULT_PARAMS = {}
DEFAULT_QUERYSTRING = {}


def event(
    body=DEFAULT_BODY,
    headers=DEFAULT_HEADER,
    method=DEFAULT_METHOD,
    pathParams=DEFAULT_PARAMS,
    queryStrings=DEFAULT_QUERYSTRING,
    **kwargs
):
    return {
        "headers": headers,
        "httpMethod": method.upper(),
        "body": body if not isinstance(body, dict) else json.dumps(body),
        "pathParameters": pathParams,
        "queryStringParameters": queryStrings,
    }


def context():
    return {}


def gateway(**kwargs):
    ev = event(**kwargs)
    ctx = context()
    return ev, ctx
