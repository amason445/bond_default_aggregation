# Bond Default Probability Aggregation
## Summary
This repository contains a class module that aggregates the total default distribution of a bond portfolio based on credit rating derived default rates and portfolio weightings. Each credit rating produces an independent number of defaults based on a [Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution). For a given number of bonds, each bond will have a different default rate based on its credit rating. Therefore, it is possible to aggregate the total default distribution by weighting each segment probability distribution based on it's portfolio weighting:

`P(X = n) = ∑ P(Ratingᵢ) × P(X = n | Ratingᵢ)`

This conforms to the [Law of Total Probability](https://en.wikipedia.org/wiki/Law_of_total_probability) since the defaults are weighted by credit rating. So, this model assumes the following:
- Bond Defaults are independent
- Default rates are derived from credit rating
- Portfolio weights by rating accurate reflect the underlying investment portfolio

## Input Parameters
The below table is arbitrarily defined and used to define the structure of the portfolio. It is defined and brought into the module as a dictionary. Since the module iterates over this dynamically, more or less credit ratings could be addes to the input. Currently, the most important factors are the Portfolio Weight and the Default Rate.
| Credit Rating | Portfolio Weight | Default Rate |
|---------------|--------|--------------|
| AAA           | 0.40   | 0.025        |
| AA            | 0.30   | 0.040        |
| A             | 0.20   | 0.060        |
| BBB           | 0.10   | 0.080        |

```python
portfolio = {'AAA': {'weight': 0.40, 'default_rate': 0.025}, 'AA': {'weight': 0.30, 'default_rate': 0.04}, 
             'A': {'weight': 0.20, 'default_rate': 0.06}, 'BBB': {'weight': 0.10, 'default_rate': 0.08}}
```
## Output
Currently, this module produces a list of tuples that can be unpackaged containing each probability for P(X = n) and the number of defaults. It can be graphed like below:

![alt_text](https://github.com/amason445/bond_default_aggregation/blob/main/DefaultFrequency.png)
