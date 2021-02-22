_Please do not publish your solution publicly (especially if you fork this repository)._

# Challenge: Sold Price Map

## Guidelines

- Aim to spend **no more than 3 hours** on the challenge (hint - we're looking for informed decisions around scope, and a minimum viable solution instead of an "all-the-bells-and-whistles" solution). We are wary of your personal time and account for this. We would rather see de-scoping than hours and hours of extra work!
- Our [Engineering Principles](https://engineering.land.tech/principles)... to give context as to how we work
- We value simplicity... "less is more"
- We value elegant solutions and clean code
- We **_really_** value tests (especially test-driven code as it is central to how we work!)
- We value clean, concise, understandable documentation (a `README.md` is sufficient) as part of communication and an entry point to the solution. Remember "less is more".
- We would like to be able to run the code as if developing locally
- Assume we may not have certain dependencies installed on our laptops!

There is no restriction on the technology stack you choose to use, however bear in mind that we use mostly work in node.js, python, shell and docker, and we're heavily influenced by DevOps principles. If in doubt, keep it simple - we like simplicity!

## The Problem

You have been given a [set of data points](sold-price-data.txt), with each item taking the following form:

```text
X Y P
```

Where:

- `0 <= X < 100`
- `0 <= Y < 100`
- `10000 < P < 10000000`

`X` and `Y` represent the coordinates of a house which has been sold, and `P` is the price in which it was sold. For example, the point "`5 10 100000`" would be interpreted as a house sold for £100,000 at the point `(5, 10)`.

Using this data plot each point on a grid. The points should be filled with a colour representing how expensive a house was in relation to other houses. The choice of colour is up to you, however, you should use a different colour for each of the following groups:

- 0% - 5%
- 5% - 25%
- 25% - 75%
- 75% - 95%
- 95% - 100%

## Technical Specification

Your system architecture should be split between a back-end and a web front-end, for instance, providing a JSON RESTful API (but feel free to be more creative or simplistic than that). You may use any other technologies provided that the general client/service architecture is respected.
