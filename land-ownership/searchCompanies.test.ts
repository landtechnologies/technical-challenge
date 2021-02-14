import { CompanyLand, CompanyRelation, searchCompanies } from './land-cli'
import Mock = jest.Mock

const mockCompaniesRelations: CompanyRelation[] = [
  {
	companyId: '5',
	name: 'fifth company',
	parentId: '2'
  },
  {
	companyId: '6',
	name: 'sixth company',
	parentId: '2'
  },
  {
	companyId: '3',
	name: 'third company',
	parentId: '1'
  },
  {
	companyId: '4',
	name: 'fourth company',
	parentId: '1'
  },
  {
    companyId: '2',
	name: 'second company',
	parentId: '0'
  },
  {
    companyId: '1',
	name: 'first company',
	parentId: '0'
  },
  {
	companyId: '0',
	name: 'first parent company',
	parentId: undefined
  }
]

const mockCompaniesLands: CompanyLand[] = [
  {
    companyId: '0',
	landId: 'landForCompany0'
  },
  {
    companyId: '1',
	landId: 'landForCompany1'
  },
  {
	companyId: '2',
	landId: 'landForCompany21'
  },
  {
	companyId: '2',
	landId: 'landForCompany22'
  }
]

test('throws error if no company relations are passed', () => {
  try {
	searchCompanies(
	  [],
	  mockCompaniesLands,
	  '0'
	)
  } catch (error) {
	expect(error.message).toBe('Invalid companyRelations parameter.')
  }
})
test('throws error if no company lands are passed', () => {
	try {
	  searchCompanies(
		mockCompaniesRelations,
		undefined,
		'0'
	  )
	} catch (error) {
	  expect(error.message).toBe('Invalid companyLands parameter.')
	}
})
test('throws error if no company id is passed', () => {
  try {
	searchCompanies(
	  mockCompaniesRelations,
	  mockCompaniesLands,
	  undefined
	)
  } catch (error) {
	expect(error.message).toBe('Invalid companyId parameter.')
  }
})
test('logs correctly for companyId 0', () => {
  console.log = jest.fn()
  searchCompanies(
	mockCompaniesRelations,
	mockCompaniesLands,
	'0'
  )
  expect(console.log).toHaveBeenCalledTimes(3)
  expect((console.log as Mock).mock.calls[0][0]).toBe(
    'Company: first parent company(0) owns 4 land(s).'
  )
  expect((console.log as Mock).mock.calls[1][0]).toBe(
	'  |-Company: first company(1) owns 1 land(s).'
  )
  expect((console.log as Mock).mock.calls[2][0]).toBe(
	'  ||-Company: fourth company(4) owns 0 land(s).'
  )
})
test('logs correctly for companyId 1', () => {
  console.log = jest.fn()
  searchCompanies(
	mockCompaniesRelations,
	mockCompaniesLands,
	'1'
  )
  expect(console.log).toHaveBeenCalledTimes(2)
  expect((console.log as Mock).mock.calls[0][0]).toBe(
    'Company: first company(1) owns 1 land(s).')
  expect((console.log as Mock).mock.calls[1][0]).toBe(
    '  |-Company: fourth company(4) owns 0 land(s).')
})
