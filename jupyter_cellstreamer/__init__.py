from .co_cellmagic import CaptureMagic
from IPython import get_ipython

try:
    ipy = get_ipython()
    ipy.register_magics(CaptureMagic)

except AttributeError:
    print("Can not load CaptureMagic because this is not a notebook")