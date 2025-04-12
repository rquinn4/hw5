# PHYS305 Homework Set #5

Welcome to the repository for **Homework Set #5** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we've covered.
The submission cutoff time is at **Tuesday Apr 17th, 11:59pm** Arizona
time.
Please use [this link](https://classroom.github.com/a/______) to
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
