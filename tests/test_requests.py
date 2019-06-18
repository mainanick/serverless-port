import pytest
from stockist.request import Request
from stockist import fn
from . import aws





def test_handler_defaults_to_aws():
    @fn()
    def handler_return_request(req):
      return req
    
    event, context = aws.gateway()
    req = handler_return_request(event, context)
    assert isinstance(req, Request)

def test_raises_not_implemented_invalid_vendor():
    
    @fn("SOINVALID")
    def raise_invalid_handler(req):
        return req
    
    with pytest.raises(NotImplementedError):
      raise_invalid_handler()