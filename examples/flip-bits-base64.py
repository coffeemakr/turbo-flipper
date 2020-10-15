import sys
# Insert the path of the executor (the root of the project) to the search path
sys.path.insert(0, '.')

from flip import Template, Base64, flip_bits

def queueRequests(target, wordlists):
    value = target.baseInput.encode('utf-8')

    generator = Template(value, flip_bits, transformations=[Base64()])

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
