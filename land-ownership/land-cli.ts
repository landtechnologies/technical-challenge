import { readFile } from 'fs'

export interface CompanyRelation {
  companyId: string
  name: string
  parentId?: string
}

export interface CompanyLand {
  companyId: string
  landId: string
}

function readCompaniesRelationsPromise(): Promise<CompanyRelation[] | void> {
  return new Promise((resolve, reject) => readFile('./company_relations.csv', 'utf8', (error, data: Buffer) => {
    if (error) {
      console.error('Error while reading ./company_relations', error)
      return reject(error)
    }
    return resolve(
      data.toString()
      .split("\n")
      .slice(1) // header row
      .map((line) => {
        const [companyId, name, parentId] = line.split(",")
        return {
          companyId, name, parentId
        }
      })
    )
  }))
}

function readCompaniesPromise(): Promise<CompanyLand[] | void> {
  return new Promise((resolve, reject) => readFile('./land_ownership.csv', 'utf8', (error, data: Buffer) => {
    if (error) {
      console.error('Error while reading ./land_ownership', error)
      return reject(error)
    }
    return resolve(
      data.toString()
      .split("\n")
      .slice(1)
      .map((line) => {
        const [landId, companyId] = line.split(",")
        return {
          landId, companyId
        }
      })
    )
  }))
}

async function loadCompaniesData() {
  const [companiesRelations, companiesLands] = await Promise.all([
    readCompaniesRelationsPromise(),
    readCompaniesPromise()
  ])
  if (!companiesLands || !companiesRelations) {
    throw new Error('Undefined returned from reading files.')
  }

  return {
    companiesRelations,
    companiesLands
  }
}

function getSubCompanyLands(
  companyRelations: CompanyRelation[],
  companyLands: CompanyLand[],
  companyId: string
): number {
  const subCompanies = companyRelations.filter(subCompany =>
    subCompany.parentId === companyId
  )
  let totalLand: number = companyLands.filter(companyLand =>
    companyLand.companyId === companyId
  ).length
  while (subCompanies.length > 0) {
    const subCompany = subCompanies.pop()
    totalLand += getSubCompanyLands(
      companyRelations,
      companyLands,
      subCompany.companyId
    )
  }
  return totalLand
}

function getTopParentCompany(
  companyRelations: CompanyRelation[],
  companyId: string
): string {
  const foundCompany = companyRelations.find(
    company => company.companyId === companyId
  )
  if (foundCompany.parentId) {
    return getTopParentCompany(
      companyRelations,
      foundCompany.parentId
    )
  }
  return companyId
}

export async function searchCompanies(
  companyRelations: CompanyRelation[],
  companyLands: CompanyLand[],
  companyId: string,
  level: number = 0
) {
  if (!companyRelations || companyRelations.length === 0) {
    throw new Error('Invalid companyRelations parameter.')
  }

  if (!companyLands || companyLands.length === 0) {
    throw new Error('Invalid companyLands parameter.')
  }

  if (!companyId) {
    throw new Error('Invalid companyId parameter.')
  }

  const subCompanies: string[] = []
  const topCompany = companyRelations.find(
    company => company.companyId === companyId
  )
  if (level === 0) {
    console.log(
      `Company: ${topCompany.name}(${topCompany.companyId}) owns `
      + `${getSubCompanyLands(companyRelations, companyLands, companyId)} land(s).`
    )
  } else {
    console.log(
      `  ` + `|`.repeat(level) + `-Company: ${topCompany.name}(${topCompany.companyId}) owns `
      + `${getSubCompanyLands(companyRelations, companyLands, companyId)} land(s).`
    )
  }
  companyRelations.map(company => {
    if (company.parentId === companyId) {
      subCompanies.push(company.companyId)
    }
  })
  while (subCompanies.length > 0) {
    const companyId = subCompanies.pop()
    await searchCompanies(
      companyRelations,
      companyLands,
      companyId,
      level + 1
    )
  }
}

async function findCompanyHoldings(companyId: string) {
  const {
    companiesLands,
    companiesRelations
  } = await loadCompaniesData()
  const topCompanyId = getTopParentCompany(companiesRelations, companyId)
  await searchCompanies(companiesRelations, companiesLands, topCompanyId)
}

(async function main() {
  const companyId = process.argv[2]
  if (!companyId) {
    throw new Error('No companyId provided after search command.')
  }
  console.log('Searching for companyId:', companyId)
  await findCompanyHoldings(companyId)
})()
