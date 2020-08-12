# Challenge: EPC Data Import

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

## Getting Started

- This problem uses real data that we already import into our application regularly
- Register a user at [epc.opendatacommunities.org](https://epc.opendatacommunities.org/#register) so that you can access the EPC data
- This challenge is concerned with the "Domestic EPC". There is a downloadable zip (~3Gb+) for around 18,000,000 EPC records.

## The Problem

We'd like to import the data as part of a regular, repeatable, automated data pipeline.

- Within the zip, we want to import data from all the `certificates.csv` files
- Within each `certificates.csv` we only want the columns `LMK_KEY`, `LODGEMENT_DATE`, `TRANSACTION_TYPE`, `TOTAL_FLOOR_AREA`, `ADDRESS`, `POSTCODE`, all other columns can be ignored.
- We'd like to write the results to a database (can be any flavour of database you prefer)

## Scope

- We have AWS resources and a Kubernetes cluster (including an ELK stack and Prometheus) at our disposal (that can be included as part of your decisions and solutions). Keep in mind we're heavily influenced by DevOps principles and practices.
- The data changes/updates every quarter and may increase in size
- For each EPC entry we have to call an external API with the `ADDRESS` column to get a lat/lng. This API isn't provided nor do you need to code for it, but do be aware that the response time is 250ms for a single request when designing your solution. You can assume the API can happily handle a hundreds of requests a second.

## Requirements

We'd like to see how you would approach this problem, from getting the data to loading it into a database. As part of this we would expect to see:

- A proof of concept, some code/execution and explanation/diagrams etc...
- What tools/resources you would use?
- How would you treat/manage the import as part of your operational workload
- How you would scale the import if it grew massively in size? Say from 8Gb to 100Gb
- How often would you run the import? What is an acceptable completion time?
- How would you know when the import has failed?
- We don't expect everything to be included in code. Aspects of your solution (such as scaling) can be described using whatever means you feel best gets the design across (a picture is a 1,000 words etc...)
