import sys
import os

print('before')

os.system(' '.join(sys.argv[1:]))

print('after')