

class Database(object):

	def __init__(self, name):
		name = self.name
		

class Table(object):

	def __init__(self, name, database, schema):
		name = self.name
		database = self.database
		schema = self.schema
		
	def

opportunity_detail_schema = {'ID':'int',
							'name':'nvarchar(255)',
							'stage':'nvarchar(100)',
							'amount':'decimal(28,10)',
							'probability':'float',
							'closeDate':'nvarchar(255)',
							'type':'nvarchar(255)',
							'category':'nvarchar(255)',
							'owner':'nvarchar(255)',
							'createdOn':'datetime',
							}
renewals_data_store = Database('RenewalsDataStore')
opportunity_detail = Table('OpportunityDetail', 'RenewalsDataStore', opportunity_detail_schema)





