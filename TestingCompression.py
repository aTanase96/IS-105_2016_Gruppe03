import pylzma
import matlab


def lzma_compression_ratio(test_string):
    line = lzma.encode()
    bytes_in = bytes(test_string)
    bytes_out = test.compress(bytes_in)
    return len(bytes_out)/len(bytes_in)


test_string = open('https://www.gutenberg.org/files/51334/51334-0.txt')
compression_ratio = lzma_compression_ratio(for line in test_string)
print(compression_ratio)