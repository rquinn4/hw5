
import numpy as np
import bilby
from bilby.core.prior import PriorDict

from phys305_hw5 import Interferometer, WaveformGenerator, mcmc_sampler, stat

def main(time_of_event):
    ifo = Interferometer("H1", time_of_event)

    prior = PriorDict()
    prior['chirp_mass'] = bilby.core.prior.Uniform(20, 40, name='chirp_mass')
    prior['mass_ratio'] = bilby.core.prior.Uniform(0.5, 1.0, name='mass_ration')


    duration = 4
    sampling_frequency = 4096
    start_time = time_of_event + 2
    waveform_generator = WaveformGenerator(duration, sampling_frequency, start_time)

    likelihood = bilby.gw.likelihood.GravitationalWaveTransient(
        interferometers=[ifo],
        waveform_generator=waveform_generator,
    )

    samples_dict = mcmc_sampler(likelihood, prior, widths=[0.1, 0.01], n_steps=1000)
    sample_array = np.array([[s['chirp_mass'], s['mass_ratio']] for s in samples_dict])

    stat(sample_array, file ="corner.png")

if __name__ == "__name__":
    main(1126259462.4)
