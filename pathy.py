import os
import glob
import re
import csv
import time
from itertools import islice

# kaper = "kaper\\"
# schemat = "schemat\\"
kaper = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'kaper'))
schemat = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'schemat'))

q = os.path.dirname(os.path.abspath(__file__))

plikiKaper = [
    os.path.join(kaper, plik) for plik in os.listdir(kaper)
    if plik.endswith(".txt")
]
plikiKaper0 = glob.glob(str(kaper) + "\\*.txt")
print(os.listdir(kaper))

print(plikiKaper)
print(kaper)
print(plikiKaper0)
print(q)