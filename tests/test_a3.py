import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from phys305_hw5 import *
import numpy as np
import pytest

time_of_event = 1126259462.4
L1 = Interferometer('L1', time_of_event)

prior = bilby.core.prior.PriorDict({
    'chirp_mass'   : Uniform(name='chirp_mass',   minimum=28.0,maximum=32),
    'chirp_mass'   : Uniform(name='chirp_mass',   minimum=28.0,maximum=32),
    'mass_ratio'   : Uniform(name='mass_ratio',   minimum=0.5, maximum=1),
    'phase'        : Uniform(name="phase",        minimum=4.54-0.2, maximum=4.54+0.2),
    'geocent_time' : Uniform(name="geocent_time", minimum=time_of_event-0.01, maximum=time_of_event+0.01),
    'a_1'          :  0.0,
    'a_2'          :  0.0,
    'tilt_1'       :  0.0,
    'tilt_2'       :  0.0,
    'phi_12'       :  0.0,
    'phi_jl'       :  0.0,
    'dec'          : -1.2232,
    'ra'           :  2.19432,
    'theta_jn'     :  1.89694,
    'psi'          :  0.532268,
    'luminosity_distance' : PowerLaw(alpha=2, name='luminosity_distance', minimum=277, maximum=320, unit='Mpc', latex_label='$d_L$'),
})

likelihood = bilby.gw.likelihood.GravitationalWaveTransient(
    [L1],
    WaveformGenerator(L1.duration, L1.sampling_frequency, L1.start_time),
    priors=prior,
    time_marginalization=True, phase_marginalization=True, distance_marginalization=True)

def test_mcmc_sampler():

    samples = mcmc_sampler(likelihood, prior, [0.1, 0.01], 32)
    assert samples.shape == (32, 16)

    samples = mcmc_sampler(likelihood, prior, [0.1, 0.01], 64)
    assert samples.shape == (64, 16)
