import pandas as pd
import us

# Load the data files
softball_df = pd.read_csv('us_softball_league.tsv', sep='\t')
golf_df = pd.read_csv('unity_golf_club.csv')
companies_df = pd.read_csv('companies.csv')


# Split name into first_name and last_name
softball_df[['first_name','last_name']] = softball_df['name'].loc[softball_df['name'].str.split().str.len() == 2].str.split(expand=True)
softball_df.drop(columns=['name'], inplace=True)

# Convert date_of_birth and last_active to datetime format
softball_df['dob'] = pd.to_datetime(softball_df['date_of_birth'], format='%m/%d/%Y')
softball_df['last_active'] = pd.to_datetime(softball_df['last_active'], format='%m/%d/%Y')

# Convert states to two-character abbreviation
softball_df['state'] = softball_df['us_state'].apply(lambda x: us.states.lookup(x).abbr)

# Map company_id to company name
softball_df['company_name'] = softball_df['company_id'].map(companies_df.set_index('id')['name'])
golf_df['company_name'] = golf_df['company_id'].map(companies_df.set_index('id')['name'])

# Add source column
softball_df['source'] = 'us_softball_league'
golf_df['source'] = 'unity_golf_club'


# Standardize column names
softball_df = softball_df.rename(columns={
    'dob': 'dob',
    'last_active': 'last_active',
    'score': 'score',
    'joined_league': 'member_since',
    'state': 'state'
})

golf_df = golf_df.rename(columns={
    'first_name': 'first_name',
    'last_name': 'last_name',
    'dob': 'dob',
    'last_active': 'last_active',
    'score': 'score',
    'member_since': 'member_since',
    'state': 'state'
})



# Standardize names to proper case
softball_df['first_name'] = softball_df['first_name'].str.title()
softball_df['last_name'] = softball_df['last_name'].str.title()
golf_df['first_name'] = golf_df['first_name'].str.title()
golf_df['last_name'] = golf_df['last_name'].str.title()

# Convert dates to common format
softball_df['dob'] = pd.to_datetime(softball_df['dob']).dt.strftime('%Y/%m/%d')
softball_df['last_active'] = pd.to_datetime(softball_df['last_active']).dt.strftime('%Y/%m/%d')
golf_df['dob'] = pd.to_datetime(golf_df['dob']).dt.strftime('%Y/%m/%d')
golf_df['last_active'] = pd.to_datetime(golf_df['last_active']).dt.strftime('%Y/%m/%d')

softball_df.drop(columns=['date_of_birth'], inplace=True)
# softball_df.to_csv('softball_df.csv', index=False)
# golf_df.to_csv('golf_df.csv', index=False)


combined_df = pd.concat([softball_df, golf_df], ignore_index=True)

# Replace company_id with company name
combined_df = combined_df.merge(companies_df, left_on='company_id', right_on='id', how='left')
combined_df.drop(columns=['company_id', 'id'], inplace=True)
combined_df.rename(columns={'name': 'company_name'}, inplace=True)


# combined_df.to_csv('combined_df.csv', index=False)

combined_df.member_since = combined_df.member_since.astype(str)




# Identify suspect records
suspect_records = combined_df[combined_df['member_since'] < combined_df['dob']]
# suspect_records = combined_df[combined_df['member_since'] > combined_df['last_active']]

# Write bad records to a separate file
suspect_records.to_csv('bad_records.csv', index=False)

# Drop bad records from the main file
combined_df = combined_df[combined_df['member_since'] <= combined_df['last_active']]
combined_df = combined_df.loc[:,~combined_df.columns.duplicated()].copy()

# Save the combined master file
combined_df.to_csv('master_file.csv', index=False)