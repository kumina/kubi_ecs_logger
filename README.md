<img align="left" height="96" width="229" src="https://github.com/kumina/kubi_ecs_logger/blob/master/logo.png">

This Python module makes logging easy for your application.  
The logger outputs JSON formatted logs for ingesting into Elastic.  

The module implements the ECS (Elastic Common Schema) specification that
can be found at for quick reference:  
[ECS Field Reference](https://www.elastic.co/guide/en/ecs/current/ecs-field-reference.html#ecs-field-reference)

## Usage
```python 
# Import 
from kubi_ecs_logger import Logger, Severity

# Set some defaults in the start of your app
Logger().dev = True
Logger().severity_output_level = Severity.INFO
Logger().defaults = {
    "event": {
        "test": "test value"
    }
}

# Log loaded configuration
Logger().event(
    category="configuration",
    action="configuration loaded",
    dataset="The configuration is loaded from config.yaml"
).out(severity=Severity.INFO)

# Output
# {
#   "@timestamp": "2019-07-11T15:11:03.193759+00:00",
#   "event": {
#     "action": "configuration loaded",
#     "category": "configuration",
#     "dataset": "The configuration is loaded from config.yaml",
#     "test": "test value"  # From defaults
#   },
#   "logline": {
#     "level": "INFO"
#   }
# }

# Here is a little bit bigger example
Logger() \
    .event(category="requests", action="request received") \
    .url(path="/test", domain="test.com") \
    .source(ip="123.251.512.152") \
    .http_response(status_code=200) \
    .out(severity=Severity.INFO)

# And here is the output of this one
# {
#   "@timestamp": "2019-07-11T15:15:48.896921+00:00",
#   "event": {
#     "action": "request received",
#     "category": "requests",
#     "test": "test value"
#   },
#   "httpresponse": {
#     "status_code": "200"
#   },
#   "logline": {
#     "level": "INFO"
#   },
#   "source": {
#     "ip": "123.251.512.152"
#   },
#   "url": {
#     "domain": "test.com",
#     "path": "/test"
#   }
# }
```

## Dependencies
| name        | version |
|-------------|---------|
| marshmallow | 2.19.2  |
