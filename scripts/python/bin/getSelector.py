from Crypto.Hash import keccak
import sys

def computeSelector(func):
  k = keccak.new(digest_bits=256)
  bytes_func = str.encode(func)
  k.update(bytes_func)
  selector =  k.hexdigest()[0:8]
  print("Hex: ", selector)
  print("Int: ", int(selector, 16))

if __name__ == "__main__":
    computeSelector(sys.argv[1])