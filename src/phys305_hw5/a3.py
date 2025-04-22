import numpy as np
from tqdm import tqdm

def mcmc_sampler(likelihood, prior, widths=[0.1, 0.01], n_step = 1000):
    parameters = prior.sample()
    chirp_mass = parameters['chirp_mass']
    mass_ratio = parameters['mass_ratio']

    likelihood.parameters = parameters
    log_post = likelihood.log_likelihood() + prior.ln_prob(parameters)

    samples = []
    total_trials = 0

    pbar = tqdm(total = n_step, desc="Sampling")
    while len(samples) < n_step:
        total_trials += 1

        proposed_chirp_mass = np.random.normal(chirp_mass, widths[0])
        proposed_mass_ratio = np.random.normal(mass_ratio, widths[1])

        proposed_parameters = parameters.copy()
        proposed_parameters['chirp_mass'] = proposed_chirp_mass
        proposed_parameters['mass_ratio'] = proposed_mass_ratio

        if not prior.supports(proposed_parameters):
            continue

        likelihood.paramters = proposed_parameters
        try:
            log_post_proposed = likelihood.log_likelihood() + prior.ln_prob(proposed_parameters)

        except:
            continue
        delta_log_post = log_post_proposed - log_post
        acceptance_prob = np.exp(min(0, delta_log_post))

        if np.random.rand() < acceptance_prob:
            chirp_mass = proposed_chirp_mass
            mass_ratio = proposed_mass_ratio
            parameters = proposed_parameters
            log_post = log_post_proposed
            samples.append(parameters.copy())
            pbar.update(1)

    pbar.close()
    efficiency = n_step / total_trials
    print(f"Sampling efficiency: {efficiency:.2%}")

    return samples