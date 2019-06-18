import json

DEFAULT_HEADER = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip",
    "Cache-Control": "no-cache",
    "CDN-Loop": "cloudflare",
    "CF-Connecting-IP": "127.0.0.1",
    "CF-IPCountry": "KE",
    "CF-RAY": "kENYA1234-MBA",
    "CF-Visitor": '{\\"scheme\\ ":\\"https\\ "}',
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Desktop-Viewer": "true",
    "CloudFront-Is-Mobile-Viewer": "false",
    "CloudFront-Is-SmartTV-Viewer": "false",
    "CloudFront-Is-Tablet-Viewer": "false",
    "CloudFront-Viewer-Country": "KE",
    "Content-Type": "application/json",
    "Cookie": "uid=dd8ghjghf15uyiuyi64",
    "Host": "api.test.stockist",
    "User-Agent": "StockistRuntime",
    "Via": "1.1 stockist.stockist.notcloudfront.net (NotCloudFront)",
    "X-Amz-Cf-Id": "gYWwar-45-ghjg==",
    "X-Amzn-Trace-Id": "Root=1-6ghgj4t6-345tft54654t546",
    "X-Forwarded-For": "127.0.0.1, 127.0.0.1, 127.0.0.1",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https",
}
DEFAULT_METHOD = "POST"
DEFAULT_BODY = (
    "ewoJInF1ZXJ5IjoieyBhbGxBY2NvdW50cyB7ZWRnZXN7IG5vZGUgeyBlbWFpbCB9IH0gfSB9Igp9"
)
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
        "resource": "/stockist",
        "path": "/stockist/",
        "headers": headers,
        "httpMethod": method.upper(),
        "isBase64Encoded": kwargs.get("isBase64Encoded", True),
        "body": body if not isinstance(body, dict) else json.dumps(body),
        "pathParameters": pathParams,
        "queryStringParameters": queryStrings,
        "stageVariables": None,
        "requestContext": {
            "resourceId": "52bkfp",
            "resourcePath": "/stockist",
            "httpMethod": "POST",
            "extendedRequestId": "465u78235=",
            "requestTime": "15/May/2019:07:28:23 +0000",
            "path": "/stockist/",
            "accountId": "1",
            "protocol": "HTTP/1.1",
            "stage": "production",
            "domainPrefix": "api",
            "requestTimeEpoch": 1557905303336,
            "requestId": "1",
            "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "sourceIp": "127.0.0.1",
                "principalOrgId": None,
                "accessKey": None,
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "StockistRuntime",
                "user": None,
            },
            "domainName": "api.test.stockist",
            "apiId": "mcei54ary0",
        },
    }


def context():
    return {}


def gateway(**kwargs):
    ev = event(**kwargs)
    ctx = context()
    return ev, ctx
