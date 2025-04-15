# PHYS305 Homework Set #5

Welcome to the repository for **Homework Set #5** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we've covered.
The submission cutoff time is at **Tuesday Apr 22nd, 11:59pm** Arizona
time.
Please use [this link](https://classroom.github.com/a/9xgqBYqm) to
accept it from GitHub Classroom.


## Structure and Grading

This homework set consists of **five assignments**, each contributing
equally to your overall grade.
The grading breakdown is as follows:

1. **Automated Evaluation (50%)**:
   * Each assignment will be graded using `pytest`, an automated
     testing framework.
   * The correctness of your solutions accounts for 1 point per
     assignment (5 points in total).
   * You can run `pytest` in GitHub Codespaces or your local
     development environment to verify your solutions before
     submission.

2. **Documentation and Coding Practices (50%)**:
   * The remaining 1 point per assignment (5 points total) will be
     based on documentation and coding practices.
   * Clear and concise **documentation** of your code, including
     meaningful comments.
   * Adherence to good **coding practices**, such as proper variable
     naming, modular design, and code readability.

By following the interface and prototypes provided in each assignment
template, you can ensure compatibility with the autograding system and
maximize your score.


## Assignments

To simplify debugging and help visualize your progress, a Jupyter
notebook is provided at `demo/vis.ipynb`.
This notebook walks you through the full inference pipeline for
gravitational wave event GW150914 and helps verify that your code is
producing the correct outputs at each stage.

You can run the notebook interactively to:
* Load LIGO data
* Visualize frequency-domain strain and noise
* Construct priors and waveforms
* Evaluate likelihoods
* Sample the posterior with your own MCMC code
* Plot final parameter estimates

Each Python file in `src/phys305_hw5/` corresponds to one assignment.
The notebook will call your implementations directly, so ensure your
functions are correct and match the required interface.
Use `pytest` to validate outputs and spot common mistakes.


### **Assignment 1**: LIGO Data Loader (2 points)

Implement the function
`Interferometer(name, time_of_event, post_trigger_duration=2, duration=4, sample_rate=4096, maximum_frequency=1024)`
that:
* Downloads the strain data and PSD data using `gwpy`
* Initializes a `bilby` interferometer object
* Sets the strain data and PSD correctly for use in GW likelihood evaluations

All the steps are provide after `Getting the data: GW150914` and
before `Low dimensional analysis` in the Gravitational Wave Open Data
Workshop tutorial notebook `demo/tutorial.ipynb`.
All you need to do is to understand the steps and reorganize them into
a function.

You can check your implementation by plotting the strain and PSD in
the visualization notebook `demo/vis.ipynb`.


### **Assignment 2**: Waveform Generator (2 points)

In this assignment, you will implement the function
`WaveformGenerator(duration, sampling_frequency, start_time)`.
This function returns a `bilby.gw.WaveformGenerator` object configured
to simulate gravitational wave signals from binary black hole mergers
using the `IMRPhenomXP` waveform model.

Key Tasks:
* Instantiate a bilby.gw.WaveformGenerator with the source model:
  `frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole`
* Use waveform arguments:
  ```
  waveform_arguments = {
    'waveform_approximant': 'IMRPhenomXP',
    'reference_frequency': 100.0,
    'catch_waveform_errors': True
  }
  ```
* Set the parameter conversion function:
  `parameter_conversion = convert_to_lal_binary_black_hole_parameters`.
* Attach additional attributes to the generator object:
  ```
  g.duration = duration
  g.sampling_frequency = sampling_frequency
  g.start_time = start_time
  ```

Most of these are provided in the "Create a likelihood" section in
`demo/tutorial.ipynb`, except the last one, which is our "hack" to
make our own MCMC code work.

You can check your implementation by plotting the waveform in the
visualization notebook `demo/vis.ipynb`.


### **Assignment 3**: MCMC Sampler (2 points)

In this assignment, you'll implement a simple Metropolis-Hastings MCMC
sampler for exploring the posterior distribution of gravitational wave
parameters.
Your task is to modify the the function implement in
[lecture 20](https://ua-2025q1-phys305.github.io/20/notes.html)
`mcmc_sampler(likelihood, prior, widths=[0.1, 0.01], n_steps=1000)`
so it works for LIGO data.
Inputs:
* `likelihood`: A `bilby` likelihood object evaluating the gravitational wave signal match
* `prior`: A PriorDict used to sample and evaluate prior probability
* `widths`: A list of standard deviations for proposing new values of chirp_mass and mass_ratio (default: `[0.1, 0.01]`)
* `n_steps`: Number of accepted MCMC steps to collect (default: `1000`)

Key Tasks:
* Initialize parameters by sampling from the prior
* Evaluate the initial log posterior:
  ```
  likelihood.parameters = ...
  log_post = likelihood.log_likelihood() + prior.ln_prob(parameters)
* In a loop:
  * Propose new values for chirp_mass and mass_ratio using Gaussian
    perturbation
  * Construct a proposed parameter dictionary
  * Evaluate the new log posterior using the proposed parameters
  * Use the Metropolis-Hastings criterion to accept or reject:
    `acceptance_prob = np.exp(log_post_proposed - log_post)`
  * If accepted, update the current state and store the sample.
* Stop when n_steps accepted samples are collected
* Print the sampling efficiency

Expected Output:
* A progress bar indicating MCMC progress
* An efficiency message at the end
* Reasonable posterior samples that can be visualized with a corner
  plot in the next assignment

You can check your implementation by running your `mcmc_sampler()` in
the visualization notebook `demo/vis.ipynb`.

### **Assignment 4**: Posterior Analysis and Visualization (2 points)

In this assignment, you will implement a function to summarize and
visualize the MCMC samples from your gravitational wave inference:
`stat(samples, file=None)`.

Inputs:
* samples: A NumPy array of shape `(n_steps, n_parameters>=2)`
  containing posterior samples for `chirp_mass` and `mass_ratio`,
  returned by your MCMC sampler.
* file (optional): A file name (e.g., 'corner.png') to save the corner
  plot.
  If the default None is used, the plot is not saved.

Key Tasks:
* Print Parameter Statistics:
  For each parameter (chirp_mass and mass_ratio), compute median, 90%
  credible interval (i.e., the 5th and 95th percentiles), and print
  results like:
  `median(chirp_mass) = 30.1 with a 90% C.I = 28.5 -> 31.7`.
* Generate a Corner Plot:
  Use the corner package to plot the 2D posterior distribution of the
  two parameters.
  Include marginal distributions, parameter labels, and quantile
  markers (5%, 50%, 95%).
* Optionally Save to File: if a file name is given, save the plot.

How to Test It:
* The debug notebook will run your `stat()` function after sampling.


### Assignment 5: Full Gravitational Wave Inference Pipeline (2 points)

In this final assignment, you will bring everything together into a
full gravitational wave parameter inference pipeline.
Your task is to implement the function: `main(time_of_event)`.
This script should:
1. Load real LIGO data
2. Set up the prior
3. Generate the waveform
4. Evaluate the likelihood
5. Run your custom MCMC sampler
6. Print summary statistics and save a corner plot

Key Tasks:
* Note that all of the above steps are actually in the visualization
  notebook `demo/vis.ipynb`!
  This means you are just copying and rearranging a Jupyter Notebook
  into a script.
* To make the script executable, wrap the call in a `__main__` block
  so you can run it from the command line:
  ```
  if __name__ == "__main__":
    main(1126259462.4)
  ```

## Additional Notes

* **Collaboration**:
  You are encouraged to discuss ideas with your peers, but your
  submission must reflect your own work.
* **Help and Resources**:
  If you encounter any difficulties, please refer to the course
  materials, consult your instructor, or seek help during office
  hours.
* **Deadlines**:
  Be mindful of the submission deadline, as late submissions will not
  be accepted.

Good luck, and have fun working on the assignments!
