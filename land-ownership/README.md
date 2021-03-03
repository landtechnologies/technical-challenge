_Please do not publish your solution publicly (especially if you fork this repository)._

# Challenge: Corporate Land Ownership

## Guidelines

1. We expect you to spend **around 2 hours** on this challenge - use your time wisely, we know it's valuable!
2. Ideally use javascript or python as we can run that kind of code fairly easily. For other languages, please wrap your solution with Docker.
3. Tell us about key decisions you made and what you'd do if you had more time.
4. Keep your solution simple, making effective use of your chosen language.
5. Do provide some tests, especially around the most important logic.
6. We're not looking for production-ready enterprise-scale code (no databases or servers please).

## Background

In the UK, most land is owned by private individuals, but plenty of land is owned by companies. Here we are interested specifically in land-owning companies and their land.

Most land-owning companies are small and simple, but others exhibit complex legal structures. For example, Sainsburys (the supermarket) owns several thousand parcels of
land in England and Wales, but its top-level legal entity, "J Sainsbury PLC", only owns about 40 parcels directly, all the other land is owned by sub-companies and sub-sub-companies etc. These
corporate structures arise from company mergers and acquisitions, as well as by design (for legal/financial reasons).

## Available Data

We have provided two files of dummy data in this directory.

`company_relations.csv`:

| company id | name                               | parent |
| ---------- | ---------------------------------- | ------ |
| C2013      | Acme Land Ltd                      |        |
| C71299     | Jacksons Stores Limited            | C4012  |
| C4012      | J Sainsbury PLC                    |        |
| C45353     | Jacksons Stores Manchester Limited | C71299 |
| ...        |                                    |        |

and `land_ownership.csv`:

| land parcel id | owning company id |
| -------------- | ----------------- |
| T54343         | C4012             |
| T8871          | C4012             |
| T12130         | C2013             |
| ...            |                   |

## Task

Our real-world end-users have the following requests:

- For a particular parcel of land, tell me which company ultimately owns the land.
- For a given company, tell me how much land that company owns in total.
- Ideally, allow me to visualize the data in more depth, e.g. view parts of a company tree, with information on land ownership for each company.

However this is a tech-challenge not the real world, so we'd just like to see a really basic script backed by in-memory data
structures.

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
