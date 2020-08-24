# Challenge: Land Parcels

## Guidelines

- Aim to spend **no more than 2 hours** on the challenge. We are wary of your personal time and account for this. If you feel there's possibility to de-scope please feel free to do so (and get in touch if you're in doubt: engineering@land.tech)
- Our [Engineering Principles](https://engineering.land.tech/principles)... to give context as to how we work
- We value simplicity... "less is more"
- We value elegant solutions and clean code
- We **_really_** value tests (especially test-driven code as it is central to how we work!)
- We value clean, concise, understandable documentation (a `README.md` is sufficient) as part of communication and an entry point to the solution. Remember "less is more".
- We would like to be able to run the code as if developing locally
- Assume we may not have certain dependencies installed on our laptops!
- If you have any questions please get in touch! engineering@land.tech

There is no restriction on the technology stack you choose to use, however bear in mind that we use mostly work in node.js, python, shell and docker. If in doubt, keep it simple - we like simplicity!

## The Problem

- We render squares of land on a map
- Squares are provided as an array of `x,y` points:

  ```text
  ["x1,y1", "x2,y2"]
  ```

- Where `x` and `y` are integers, with `0 <= x < 100` and `0 <= y < 100`.

- A parcel of land is `>=1` squares that are adjacent to one another (vertically or horizontally). So for example the following squares would contain 2 parcels of land, a 1x3 parcel, and a 1x1 parcel.

  ```text
  0,0
  0,1
  0,2
  2,0
  ```

  <img  alt="diagram with 1x3 and 1x1 parcels" src="/backend/diagram.png" height=200>

- Given a random set of points, we'd like to know:
  - How many parcels of land there are
  - The number of sides each parcel has

### Parcel Number Of Sides

- Assume parcels can't have holes (ie no donut style parcels)
- Here are some examples with the number of sides:

  <img  alt="diagram with 1x3 and 1x1 parcels" src="/backend/diagram.png" height=200>
  
  - 1x3 parcel has 8 sides
  - 1x1 parcel has 4 sides

## Requirements

- A method signature of `render(points: string[]) => number[]`, ie a function that takes an array `string[]` of `x,y` points
  and returns an array `number[]`, with the n'th entry in the representing the permimeter for the n'th parcel.
- Feel free to improve the signature's understandability / readability in terms of types but try to retain the underlying concept of the signature.
- We're not overly obsessed with optimisation, but we do appreciate thoughtful choices (and reasoning / trade-offs) of data structures, iteration vs recursion, and efficiency (big O notation).
- We'd like to see clean, readable, understandable code with tests.
- We'd like to see a README as a point of entry to the problem providing us with any context or details your deem helpful
