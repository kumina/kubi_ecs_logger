# Kubi ECS Logger

![Kubi ECS logo](logo.png)

## Overview 
This Python module makes logging easy for your application.  
The logger outputs JSON formatted logs for ingesting into Elastic.  

The module implements the ECS (Elastic Common Schema) specification that
can be found at for quick reference:  
[ECS Field Reference](https://www.elastic.co/guide/en/ecs/current/ecs-field-reference.html#ecs-field-reference)

## Usage
```python 
from kubi_ecs_logger.wrapper import Logger

Logger().set_defaults({
    "error": {
        "app": "myapp"
    }
}).set_dev(True).set_severity('INFO')

Logger(message="This is my log message.").event(action="logging").out(severity='debug')
```

## Dependacies
TODO

## How to use
TODO
