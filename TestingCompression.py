import pylzma


def lzma_compression_ratio(test_string):
    line = lzma.encode()
    bytes_in = bytes(test_string)
    bytes_out = test.compress(bytes_in)
    return len(bytes_out)/len(bytes_in)

test_string = 'a man, a plan, a canal: panama'
compression_ratio = lzma_compression_ratio(test_string)
print(compression_ratio)