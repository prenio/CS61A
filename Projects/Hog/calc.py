import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
