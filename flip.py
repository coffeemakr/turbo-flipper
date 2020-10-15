import re
import base64

class ValueTransformation:
    def decode(self, value):
        raise NotImplementedError()

    def encode(self, value):
        raise NotImplementedError()

def _fix_base64_padding(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return data


class Base64(ValueTransformation):
    def __init__(self, padding = b'=', altchars=b'+/'):
        self.padding = padding
        self.altchars = altchars

    def decode(self, value):
        if not self.padding:
            value = _fix_base64_padding(value)
        else:
            value.replace(self.padding, b'=')
        return base64.b64decode(value, altchars=self.altchars)

    def encode(self, value):
        value = base64.b64encode(value, altchars=self.altchars)
        if not self.padding:
            value = value.rstrip(b'=')
        else:
            value = value.replace(b'=', self.padding)
        return value

def _decode_all(value, transformations):
    for transformation in transformations:
        value = transformation.decode(value)
    return value

def _encode_all(value, transformations):
    for transformation in reversed(transformations):
        value = transformation.encode(value)
    return value


def flip_bits(raw_value):
    '''
    Flip each bit once.
    '''
    original_byte_list = list(raw_value)
    for byte_index, byte in enumerate(original_byte_list):
        byte = ord(byte)
        for bit_index in range(8):
            new_byte = byte ^ (1 << (7 - bit_index))
            yield raw_value[:byte_index] + chr(new_byte) + raw_value[byte_index+1:]
                

class Template:
    def __init__(self, value, manipulation, start=b'', end=b'', transformations=None):
        self.start = start
        self.end = end
        self.transformations = transformations or []
        self.value = value
        self.manipulation = manipulation

    def __iter__(self):
        raw_value = _decode_all(self.value, self.transformations)
        assert self.value == _encode_all(raw_value, self.transformations)
        for new_value in self.manipulation(raw_value):
            new_value = _encode_all(new_value, self.transformations)
            yield self.start + new_value + self.end
