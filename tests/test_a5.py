import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from phys305_hw5 import *
import os

def test_main():
    main(1126259462.4)
    assert os.path.isfile('corner.png')
