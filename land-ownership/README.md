_Please do not publish your solution publicly (especially if you fork this repository)._

# Challenge: Corporate Land Ownership

## Guidelines

1. We expect you to spend **around 1.5 hours** on this challenge - use your time wisely, we know it's valuable!
2. Ideally use javascript or python as we can run that kind of code fairly easily. For other languages, please wrap your solution with Docker.
3. Tell us about key decisions you made and what you'd do if you had more time.
4. Keep your solution simple, making effective use of your chosen language.
5. Do provide some tests, especially around the most important logic.
6. We're not looking for production-ready enterprise-scale code (no databases or servers please, and keep boilerplate to a minimum).

## Background

In the UK, most land is owned by private individuals, but plenty of land is owned by companies. Here we are
interested specifically in land-owning companies and their land.

Most land-owning companies are small and simple, but others exhibit complex legal structures as a result of
company mergers and acquisitions, as well as by design (for legal/financial reasons).

For example, Sainsburys (the supermarket) _indirectly_ owns several thousand parcels of land in the UK via
sub-companies and sub-sub-companies. However its top-level legal entity, "J Sainsbury PLC", only owns about 40
parcels _directly_.

## Available Data

We have provided two files of fictitious/dummy data in this directory.

The files are fairly large and include examples of deep company trees, but the data right at the top
is really simple - it describes a fictitious UK supermarket called "Amazing Supermarket" that owns just 5
parcels of land in total across its 4 legal entities...

`company_relations.csv`:

| company id | name                         | parent |
| ---------- | ---------------------------- | ------ |
| C01        | Amazing England              | C04    |
| C02        | Amazing Wales                | C04    |
| C03        | Amazing Distribution England | C01    |
| C04        | Amazing Supermarket UK PLC   |        |
| ...        |                              |        |

and `land_ownership.csv`:

| land parcel id | owning company id |
| -------------- | ----------------- |
| T01            | C02               |
| T02            | C01               |
| T03            | C03               |
| T04            | C01               |
| T06            | C04               |
| ...            |                   |

## Task

Our real-world end-users have the following request:

**For a given company id, tell me how much land that company owns in total, both directly and indirectly.**

As this is a tech-challenge not the real world, we'd just like to see a really basic script backed by
in-memory data structures.

_Don't forget to re-read the Guidelines at the top of the page!_

## Some Useful Code Snippets

We're not that interested in how you load data from CSV or what the interface to your script is like. You can copy and paste these examples (although you're on your own if not using node or python):

**Node**

```javascript
const fs = require("fs");
fs.readFileSync("./company_relations.csv", "utf8")
  .split("\n")
  .slice(1) // header row
  .forEach((line) => {
    const [id, name, parentId] = line.split(",");
    // ... do something with the data
  });

fs.readFileSync("./land_ownership.csv", "utf8")
  .split("\n")
  .slice(1) // header row
  .forEach((line) => {
    const [landId, companyId] = line.split(",");
    // ... do something with the data
  });

...

// Hey LandTech, uncomment and modify one of these examples...
// doSomething(somethingId, somethingOptions)
// doSomethingElse()
```

**Python**

```python
with open("./company_relations.csv") as csv:
  next(csv) # header
  for line in csv:
    id, name, parentId = line.split(",")
    # ... do something with the data

with open("./land_ownership.csv") as csv:
  next(csv) # header
  for line in csv:
    landId, companyId = line.split(",")
    # ... do something with the data

...

# Hey LandTech, uncomment and modify one of these examples..
# doSomething(somethingId, somethingOptions)
# doSomethingElse()
```

_Don't forget to re-read the Guidelines at the top of the page!_
