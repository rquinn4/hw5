from phys305_hw5 import *

import numpy as np
import pytest

import io, os
from contextlib import redirect_stdout

def test_stat():

    samples = np.load('tests/data/samples.npy')

    with io.StringIO() as buf, redirect_stdout(buf):
        stat(samples, 'tests/data/corner.png')
        output = buf.getvalue()

    print(output)
    assert os.path.isfile('tests/data/corner.png')
