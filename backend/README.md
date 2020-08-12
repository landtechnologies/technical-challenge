# Challenge: Number Of Land Parcels

## Guidelines

- Aim to spend **no more than 3 hours** on the challenge. We are wary of your personal time and account for this. We would rather see de-scoping and reasoning than hours of extra work!
- Our [Engineering Principles](https://engineering.land.tech/principles)... to give context as to how we work
- We value simplicity... "less is more"
- We value elegant solutions and clean code
- We **_really_** value tests (especially test-driven code as it is central to how we work!)
- We value clean, concise, understandable documentation (a `README.md` is sufficient) as part of communication and an entry point to the solution. Remember "less is more".
- We would like to be able to run the code as if developing locally
- Assume we may not have certain dependencies installed on our laptops!

There is no restriction on the technology stack you choose to use, however bear in mind that we use mostly work in node.js, python, shell and docker. If in doubt, keep it simple - we like simplicity!

## The Problem

- We render parcels of land on map tiles
- A map tile is a multi-dimensional array of 0's and 1's
- A parcel of land is a collection of 1's that are adjacent to one another (excluding diagonally). The below simplisitic example has 4 parcels of land:

  ```text
  0 0 1 1 1 0
  0 0 0 0 0 0
  0 1 1 1 1 0
  0 1 1 0 1 0
  0 0 0 1 0 0
  1 0 0 1 1 0
  ```

- Given a random size of map tile, we'd like to know:
  - How many parcels of land are on it
  - The average size of a parcel of land (ie `1 1` == 2, `1 1 1` == 3)

## Requirements

- We're not overly obsessed with optimisation, but we do appreciate thoughtful choices (and reasoning / trade-offs) of data structures, iteration vs recursion, and efficiency such as O(n) solutions.
- We'd like to see clean, readable, understandable code with tests.
- We'd like to see a README as a point of entry to the problem providing us with any context or details your deem helpful

## Extending The Problem

- There's no expectation to solve this part in code (but feel free to should you wish).
- We'd like to understand your thought process for calculating the perimeter of a parcel of land in relation to the above solution.
- Assume parcels can't have holes (ie no donut style parcels) and diagonals are not included as part of the perimeter
- The the below examples:
  - a) has a perimeter of 4 (ie 1 x 4 sides)
  - b) has a perimeter of 8 (ie 2 x 4 sides)
  - c) has a permiter of 12 (ie 3 x 4 sides)
  - d) has 12 (ie 3 + 2 + 1 + 1 + 1 + 1 + 1 + 2)

```text
a)       b)         c)           d)
0 0 0    0 0 0 0    0 0 0 0 0    0 0 0 0 0
0 1 0    0 1 1 0    0 1 1 1 0    0 1 1 1 0
0 0 0    0 1 1 0    0 1 1 1 0    0 1 0 1 0
         0 0 0 0    0 1 1 1 0    0 0 0 0 0
                    0 0 0 0 0
```
