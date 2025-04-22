import numpy as np
import corner
import matplotlib.pyplot as plt

def stat(samples, file = None):
    samples = np.array(samples)
    if samples.ndim == 1 or samples.shape[1] < 2:
        raise ValueError("Samples must be a 2D array with at least 2 columns: chirp_mass and chirp_ratio.")
    
    labels = ["chirp_mass", "chirp_ratio"]

    for i, label in enumerate(labels):
        median = np.median(samples[:, i])
        lower = np.percentile(samples[:, i], 5)
        upper = np.percentile(samples[:, i], 95)
        print(f"median({label}) = {median:.2f} with a 90% C.I. = {lower:.2f} -> {upper:.2f}")

    fig = corner.corner(
        samples[:, 2],
        labels =labels,
        quantiles=[0.05, 0.5, 0.95],
        show_titles=True,
        title_fmt=".2f",
        title_kwargs={"fontsize": 12}
    )
    if file:
        plt.savefig(file)
        print(f"Corner plot saved to {file}")

    else:
        plt.show()
