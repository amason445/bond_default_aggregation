# Bond Default Probability Aggregation
## Summary
This repo contains a class module that aggregates the total default distribution of a portfolio of bonds by a default frequency associated with a credit rating as well as a portfolio weight. These credit ratings and portfolio weightings were arbitrarily selected but could also be derived from an actual portfolio. To calculate this aggregate, a conditional binomial distribution of the number of bond defaults is weighted by the target portfolio weighting:

`∑ P(Ratingᵢ) · P(X = n | Ratingᵢ)`

This weighting conforms to the [Law of Total Probability](https://en.wikipedia.org/wiki/Law_of_total_probability) since the defaults are weighted by credit rating.

`⋂ { P(X = n | Ratingᵢ) · P(Ratingᵢ) } = ∑ P(Ratingᵢ) · P(X = n | Ratingᵢ)`

A binomial distribution is selected because each credit rating could produce a different number of defaults based on it's default rate in the below table:
| Credit Rating | Weight | Default Rate |
|---------------|--------|--------------|
| AAA           | 0.40   | 0.025        |
| AA            | 0.30   | 0.040        |
| A             | 0.20   | 0.060        |
| BBB           | 0.10   | 0.080        |

This class module produces a list of tuples that can be unpackaged and graphed like the below:

![alt_text](https://github.com/amason445/bond_default_aggregation/blob/main/DefaultFrequency.png)
