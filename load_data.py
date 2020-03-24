from postgresql import pgEngine
import pandas as pd

# PostgreSQL connection doesn't work with Pandas so have initiated this engine as well with SQLAlchemy
engine = pgEngine()

print('Loading in csv')
# Load in cost estimation model data 
data = pd.read_csv('numbers.csv')
print('Successfully loaded csv')

print('Beginning to load data to database')
data.to_sql('wealth_mgmt_propensity',engine, schema='prototyping',if_exists='replace')
print('Successfully loaded data')