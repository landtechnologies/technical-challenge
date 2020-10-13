# Challenge: Corporate Land Ownership

## Guidelines

Spend a **maximum of 3 hours** on this challenge.

Your time is valuable, so DO focus on:

- Demonstrating clarity of thought.
- Demonstrating mastery of your chosen stack, where relevant.
- Making sure we can easily run, test, and understand your solution.

DO NOT:

- Create an entire production-ready enterprise-grade application.

You can use any tech stack, but for reference we use node.js, python, shell and docker.

You may wish to have a quick read of [Our Engineering Principles](https://engineering.land.tech/principles) and [Our Tech Radar](https://engineering.land.tech/radar/).

**If in doubt, keep it simple - we like simplicity!**

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

| land parcel id | owning company id | "   |
| -------------- | ----------------- | --- |
| T54343         | C4012             |     |
| T8871          | C4012             |     |
| T12130         | C2013             |     |
| ...            |                   |     |

## Task

End-users want a tool to visualize the corporate structure and quantity of land ownership for any given land-owning company.

We _don't_ need a "proper" user interface (a basic CLI is fine), we also _don't_ want you to spend time on infrastructure (in-memory data is fine).
Having said that, we are interested to hear how you would use infrastructure/databases if you were to productionize your solution.

Note that ultimately the solution would need to handle a few tens of requests per second, work with tens of millions of land parcels,
hundreds of thousands of companies, and company structures that contain a couple of thousand constituent legal entities.

You can take this task in any direction you believe aligns with the end-user need (and demonstrates your abilities!).
We are happy for you to make assumptions where needed, but be explicit about this. You can also get in touch with us if you wish - engineering@land.tech.

_Don't forget to re-read the Guidelines at the top of the page!_

## Suggested approach

We suggest creating a cli tool that accepts a company id and prints out a partially-expanded tree like this:

```
> landtree --mode=from_root C45353
C4012; J Sainsbury PLC; owner of 400 land parcels
  | -  C12332; Sainsbury London; owner of 100 land parcels
  | -  C71299; Jacksons Stores Limited; owner of 14 land parcels
  | | - C45353; Jacksons Stores Manchester Limited; owner of 2 land parcels ***
  | | - C91123; Jacksons Stores Coventry Limited; owner of 1 land parcel
  | - C555123; Best products; owner of 13 land parcels
  | - C712933; 24 Hour Food Local Norfolk; owner of 1 land parcels
```

Note how we specify `--mode=from_root`, which provides the tree "from the root" down to the company in question, leaving other areas of the tree not expanded.
The "owner of X land parcels" bit states the total count of all parcels owned by the company and its sub companies.

The next step might be to support expanding parts of the tree. For example:

```
> landtree --mode=expand C555123
| - C623354; Best products Children Ltd; owner of 2 land parcels
| - C555123; Best products Metro; owner of 9 land parcels
```

We're not overly obsessed with optimisation, but we do appreciate thoughtful choices (and reasoning / trade-offs) of data structures, iteration vs recursion, and efficiency (big O notation).

_Don't forget to re-read the Guidelines at the top of the page!_

## Bonus considerations

Company relationships can be messy - one company may have shared corporate ownership, with the parent companies possibly appearing in multiple places in the tree.
Somewhat surprisingly there can even been cycles within relations, with two companies owning part of each other (although this is rare). Note that the sample company relations do not have these
complications, but you are welcome to modify the sample data if you want to take the task closer to the real-world problem.

Most end-users are interested in only specific regions within England or Wales. Assuming we have data about the location of each land parcel, how would you
extend the above task to provide information that is valuable on the local level?
