# Bond Default Probability Aggregation
## Summary
This repo contains a class module that aggregates the total default distribution of a portfolio of bonds by a default frequency associated with a credit rating as well as a portfolio weight. These credit ratings and portfolio weightings were arbitrarily selected but could also be derived from an actual portfolio. To calculate this aggregate, a conditional binomial distribution of the number of bond defaults is weighted by the target portfolio weighting:

$$
\sum P(\text{Credit Rating}) \cdot P(X = n \mid \text{Credit Rating})
$$

This weighting conforms to the [Law of Total Probability](https://en.wikipedia.org/wiki/Law_of_total_probability) since the defaults are weighted by credit rating.

$$
\bigcap_{i} \left\{ P(X = n \mid \text{Rating}_i) \cdot P(\text{Rating}_i) \right\}
= \sum_{i} P(\text{Rating}_i) \cdot P(X = n \mid \text{Rating}_i)
$$

This class module produces a list of tuples that can be unpackaged and graphed like the below: