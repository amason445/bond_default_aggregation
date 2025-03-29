import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from collections import defaultdict

class BondDefaults:
    def __init__(self, portfolio: dict, n_bonds: int):
        self.portfolio = portfolio
        self.n_bonds = n_bonds

    def total_default_probability(self) -> list[tuple[int,float]]:
        #aggregate default distributions by credit segment
        r_values = list(range(self.n_bonds + 1))   
        segment_probabilities = []
        for key, value in self.portfolio.items():
            credit_segment_dist = [binom.pmf(r, self.n_bonds, value['default_rate']) * value['weight'] for r in r_values]
            default_tuples = list(zip(r_values, credit_segment_dist))
            segment_probabilities.append(default_tuples)

        #map and reduce credit segments by summation to find the total default distribution
        result = defaultdict(int)
        for sublist in segment_probabilities:
            for key, value in sublist:
                result[key] += value 
        reduced_list = sorted(result.items())
        return reduced_list

if __name__ == "__main__":
    portfolio = {'AAA': {'weight': 0.40, 'default_rate': 0.025}, 'AA': {'weight': 0.30, 'default_rate': 0.04}, 
                 'A': {'weight': 0.20, 'default_rate': 0.06}, 'BBB': {'weight': 0.10, 'default_rate': 0.08}}
    n_bonds = 100
    default_probability = BondDefaults(portfolio, n_bonds).total_default_probability()
    
    x, y = zip(*default_probability)  
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    axs[0].plot(x, y)
    axs[0].set_title("Original Default Probabilities")
    axs[0].grid(True)
    axs[1].plot(x, np.log10(np.array(y) + 1e-10))
    axs[1].set_title("Log-Transformed Default Probabilities")
    axs[1].grid(True)
    plt.xlabel("Number of Bond Defaults")
    plt.suptitle(f"Default Probability for {n_bonds} Bonds Weighted by Credit Rating")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("DefaultFrequency.png")