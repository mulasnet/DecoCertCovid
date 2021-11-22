import pprint
from urllib.parse import unquote    # Si el codigo encriptado aparece sin " % " comentar la linea
from base45 import b45decode
import zlib
import cbor2

data = "codigo_encriptado"
data = unquote(data)                # Si el codigo encriptado aparece sin " % " comentar la linea
data = data.replace ("HC1:", "")
z_data = b45decode(data)
databytes = bytes(z_data)
decompress = zlib.decompress(databytes)
decoded = cbor2.loads(decompress)

pprint.pprint(cbor2.loads(decoded.value[2]))