import base64
import json

import pytest

from stockist import fn
from stockist.request import Request

from . import aws


@fn()
def handler_return_request(req):
    return req


def test_handler_defaults_to_aws():
    event, context = aws.gateway()
    req = handler_return_request(event, context)
    assert isinstance(req, Request)


def test_raises_not_implemented_invalid_vendor():
    @fn("SOINVALID")
    def raise_invalid_handler(req):
        return req

    with pytest.raises(NotImplementedError):
        raise_invalid_handler()


def test_has_valid_request_body_passed():
    body = {"name": "bodyisvalid"}
    event, context = aws.gateway(body=body)
    req = handler_return_request(event, context)
    assert req.body["name"] == body["name"]


def test_has_valid_request_body_if_base64d():
    body = {"name": "body64"}
    _body = base64.b64encode(bytes(json.dumps(body), encoding="utf-8"))
    event, context = aws.gateway(body=_body, isBase64Encoded=True)
    req = handler_return_request(event, context)
    assert req.body["name"] == body["name"]
