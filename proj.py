import pandas as pd

'''
Notes:
    - instead of dates might be better to use age/time since transaction
    - loan status -1 -> bad; 1 -> good
'''

# FUNCTIONS

# Format birth number to date (DD-MM-YY) <- may need to change formatting for algorithms
def get_formatted_date_from_birth_number(date_number):
    date_number_string = str(date_number)
    return date_number_string[4:6] + '-' + str(int(date_number_string[2:4]) % 50) + '-' + date_number_string[0:2]

# Get client sex from birth number (MM > 50 => sex == 'F')
def get_client_sex_from_birth_number(date_number):
    return 'F' if int(str(date_number)[2:4]) >= 51 else 'M'

# DATAFRAMES

client_df = pd.read_csv('.\\ficheiros_competicao_dev\\client.csv', sep=';')

# DATA PROCESSING

#print(client_df.to_string())

client_df['birthday'] = client_df['birth_number'].apply(get_formatted_date_from_birth_number)

client_df['sex'] = client_df['birth_number'].apply(get_client_sex_from_birth_number)

client_df = client_df.drop(columns=['birth_number'])

print(client_df.head())
