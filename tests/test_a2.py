from phys305_hw5 import *
import numpy as np
import pytest

time_of_event = 1126259462.4
L1 = Interferometer('L1', time_of_event)
waveform_generator = WaveformGenerator(
    L1.duration, L1.sampling_frequency, L1.start_time)

@pytest.mark.parametrize("param", [{
        'chirp_mass': 28.49789522719009,
        'mass_ratio': 0.9831667496041587,
        'phase': 4.536795834268788,
        'geocent_time': 1126259462.3902996,
        'luminosity_distance': 317.6057364828962,
        'postfix': 1,
    }, {
        'chirp_mass': 29.446845530802605,
        'mass_ratio': 0.8203352839266134,
        'phase': 4.726789738552674,
        'geocent_time': 1126259462.3947268,
        'luminosity_distance': 285.18184021350135,
        'postfix': 2,
    }])
def test_waveform(param):

    postfix = param.pop('postfix')
    sample = {
        'a_1': 0.0,
        'a_2': 0.0,
        'tilt_1': 0.0,
        'tilt_2': 0.0,
        'phi_12': 0.0,
        'phi_jl': 0.0,
        'dec': -1.2232,
        'ra': 2.19432,
        'theta_jn': 1.89694,
        'psi': 0.532268,
        **param
    }

    waveforms = waveform_generator.frequency_domain_strain(sample)
    plus_ref  = pytest.approx(np.load(f'tests/data/plus{postfix}.npy'))
    cross_ref = pytest.approx(np.load(f'tests/data/cross{postfix}.npy'))

    assert waveforms['plus']  == plus_ref
    assert waveforms['cross'] == cross_ref
