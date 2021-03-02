_Please do not publish your solution publicly (especially if you fork this repository)._

# Challenge: Corporate Land Ownership

## Guidelines

Spend a **maximum of 2 hours** on this challenge.

Your time is valuable, so DO FOCUS ON:

- Demonstrating clarity of thought.
- Demonstrating mastery of your chosen language.
- Making sure your solution is easy to run, easy to understand, and the most important logic is well-tested.

We are NOT LOOKING FOR:

- Extensive configuration/boilerplate code.
- Production-readiness.
- Enterprise-readiness.

You can use any tech stack, but we're best setup to run node.js or python submissions. If you use another language ideally wrap your solution with docker.

You may wish to have a (very quick) read of [Our Engineering Principles](https://engineering.land.tech/principles) and [Our Tech Radar](https://engineering.land.tech/radar/).

Particularly in this tech-challenge scenario, **less is more**.

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

(a) For a particular parcel of land, tell me which company ultimately owns the land.  
(b) For a given company, tell me how much land that company owns in total.  
(c) Ideally, allow me to visualize the data in more depth, e.g. view parts of a company tree, with information on land ownership for each company.  

However this is a tech-challenge not the real world, so we'd just like to see a really basic script backed by in-memory data
structures (no servers or databases please).

It's ok to make assumptions, but do tell us why you went in a particular direction (you can also email us - engineering@land.tech).

_Don't forget to re-read the Guidelines at the top of the page!_

Loading CSVs into memory isn't terribly exciting, so we suggest just copy-pasting one of these snippets and then moving on to the core of the problem:

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
```

_Don't forget to re-read the Guidelines at the top of the page!_

 You can build a proper command line interface to your script if you like, but it's absolutely ok to simply hard 
 code one or more examples at the bottom of your code...
 
```javascript
... 

// Hey LandTech, uncomment and modify one of these examples..
// printUltimateOwner(<land_id>)
// printTotalOwnership(<company_id>)
// printTree(<company_id>, <tree rendering options>)
```
 
## Bonus Considerations

If you have time, we would be interested in your thoughts (just thoughts) on the real-world scenario. Note that ultimately the solution would need to handle a few tens of requests per second, work with tens of millions of land parcels, hundreds of thousands of companies, and company structures that contain a couple of thousand constituent legal entities.

Also, the real-world data is messier than the sample data here. You might like to consider one or more of the following real-world cases:

- company X is owned 50% by company Y and 50% by company Z.
- company X is owned 50% by each of Y and Z, but Z also owns 25% of company Y.
- company X is 25% owned by company Y, but company Y is 25% owned by company X (this does happen!)

You could also think about other features that the end-user might need. For example, end users might want to know about ownership within a very specific region of the country rather than the whole UK.

_Don't forget to re-read the Guidelines at the top of the page!_
