# Turbo Flipper
A script to simplify bit manipulation that can be used in turbo intruder. The code is therefore Python 2 (Jython) compatible.

## Usage
Get the latest turbo intruder jar from [their release page](https://github.com/PortSwigger/turbo-intruder/releases) and run the example from the root directory:
```
java -jar turbo-intruder-all.jar examples/flip-bits-base64.py request.txt http://localhost:8000  YWJjZGVmZ2hpams=
```

```
ID | Word | Status | Wordcount | Length | Time
Starting attack...
Warming up...
1 | YeJjZGVmZ2hpams= | 404 | 246 | 653 | 3
4 | ZWJjZGVmZ2hpams= | 404 | 246 | 653 | 4
2 | 4WJjZGVmZ2hpams= | 404 | 246 | 653 | 1
3 | IWJjZGVmZ2hpams= | 404 | 246 | 653 | 5
5 | QWJjZGVmZ2hpams= | 404 | 246 | 653 | 1
6 | Y2JjZGVmZ2hpams= | 404 | 246 | 653 | 4
8 | YWJjZGVmZ2hpams= | 404 | 246 | 653 | 0
7 | cWJjZGVmZ2hpams= | 404 | 246 | 653 | 2
9 | aWJjZGVmZ2hpams= | 404 | 246 | 653 | 5
11 | YGJjZGVmZ2hpams= | 404 | 246 | 653 | 3
```

## Scripting

```py
# add flip.py location to the path or simply copy paste the content 
import sys
sys.path.insert(0, '.')

# import what you need
from flip import Template, Base64

def generate(decoded_value):
    '''
    my maniplation function. If you perform transformations, 
    you will receive the decoded base value as the first parameter.
    '''
    for i in range(10):
        yield decoded_value + str(i)

def queueRequests(target, wordlists):
    value = target.baseInput.encode('utf-8')

    generator = Template(value, generate, transformations=[Base64()])

    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=1,
                           pipeline=False
                           )
    
    engine.queue(target.req, value)
    
    for req in generator:
        engine.queue(target.req, req)

    
def handleResponse(req, interesting):
    table.add(req)
```
