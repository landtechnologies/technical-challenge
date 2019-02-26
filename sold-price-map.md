# Challenge: Sold Price Map

## Problem 1
You have been given a [set of data points](sold-price-data.txt), with each item taking the following form:

```
X Y P
```

where `0 <= X < 100` and `0 <= Y < 100`, and `0 < P < 10000000`.
`X` and `Y` represent the coordinates of a house which has been sold, and `P` is the price in which it was sold. For example, the point "`5 10 100000`" would be interpreted as a house sold for £100,000 at the point `(5, 10)`.

Using this data plot each point on a grid. The points should be filled with a colour representing how expensive a house was in relation to other houses. The choice of colour is up to you, however, you should use a different colour for each of the following groups:
  - 0% - 5%
  - 5% - 25%
  - 25% - 75%
  - 75% - 95%
  - 95% - 100%

For back-end or terminal solutions, how you represent colour for each point is up to you.

## Technical specification
Your system architecture should be split between a back-end and a web front-end, for instance, providing a JSON in/out RESTful API. Feel free to use any other technologies provided that the general client/service architecture is respected.

Choose **one** of the following flavours that best suits the role you are applying for:

1. **Full stack**: include both front-end and back-end implementation.
1. **Back-end**: include a minimal front-end (e.g. a static view or API docs). Write, document and test your API as if it will be used by other services.
1. **Front-end**: include a minimal back-end, or use the sample data included directly. Focus on making the interface as polished as possible.
1. **Junior**: As much as you feel confident with - a terminal only solution is perfectly acceptable.