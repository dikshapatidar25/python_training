import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#packagesample

import extra.iota
print(extra.iota.funI())

from extra.iota import funI as funIota
print(funIota())
 
from extra.iota import funI
print(funI())