# Stockist

Avoid serverless vendor locking

```python
>>> import stockist

@stockist.fn(provider="aws") # returns like flask request
def handler(request):
    if request.body.get("vendor", None) is None:
        return "not_available"
    return "available"



@stockist.fn(provider="gcp") # GCP uses flask returns flask request
def log(request):
    # my_logging_fn(request.body.get("q", None))
    return 1
```
