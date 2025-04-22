
from src import 
import bilby
import numpy as np
import pytest

time_of_event = 1126259462.4
L1 = Interferometer('L1', time_of_event)

def test_interferometer():
    assert isinstance(L1, bilby.gw.detector.interferometer.Interferometer)

def test_strain():
    strain     = L1.strain_data.frequency_domain_strain
    strain_ref = pytest.approx(np.load('tests/data/strain.npy'))
    assert strain == strain_ref

def test_psd():
    psd     = L1.power_spectral_density.asd_array
    psd_ref = pytest.approx(np.load('tests/data/psd.npy'))
    assert psd == psd_ref

def test_mask():
    mask = L1.strain_data.frequency_mask
    assert len(mask) == 8193 and np.sum(mask) == 4017
