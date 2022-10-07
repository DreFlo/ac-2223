import pandas as pd

'''
Notes:
    - instead of dates might be better to use age/time since transaction
    - loan status -1 -> bad; 1 -> good
'''

# FUNCTIONS

# Format birth number to date (DD-MM-YY) <- may need to change formatting for algorithms
def get_formatted_date(date_number):
    date_number_string = str(date_number)
    return date_number_string[4:6] + '/' + str(int(date_number_string[2:4]) % 50) + '/' + '19' + date_number_string[0:2]

# Get client sex from birth number (MM > 50 => sex == 'F')
def get_client_sex_from_birth_number(date_number):
    return 'F' if int(str(date_number)[2:4]) >= 51 else 'M'

# DATAFRAMES

client_df = pd.read_csv('.\\ficheiros_competicao_dev\\client.csv', sep=';')

# DATA PROCESSING

#print(client_df.to_string())
'''
client_df['birthday'] = client_df['birth_number'].apply(get_formatted_date_from_birth_number)

client_df['sex'] = client_df['birth_number'].apply(get_client_sex_from_birth_number)

client_df = client_df.drop(columns=['birth_number'])

print(client_df.head())
'''

trans_df = pd.read_csv('.\\ficheiros_competicao_dev\\trans_dev.csv', sep=';', low_memory=False)

trans_df['date'] = pd.to_datetime(trans_df['date'].apply(get_formatted_date), infer_datetime_format=True)

loan_df = pd.read_csv('.\\ficheiros_competicao_dev\\loan_dev.csv', sep=';', low_memory=False)

loan_df['date'] = pd.to_datetime(loan_df['date'].apply(get_formatted_date), infer_datetime_format=True)

#trans_df = trans_df[['account_id', 'amount', 'balance']].groupby(['account_id']).mean()

def nearest(items, pivot):
    min_list = [i for i in items if i <= pivot]
    if (min_list == []): return 0
    return pd.to_datetime(min(min_list, key=lambda x: abs(x - pivot)))

def get_balance_at_date(row):

    account = row['account_id']
    date = row['date']

    account_trans = trans_df[trans_df['account_id'] == account]

    print(account_trans)

    nearest_date = nearest(account_trans['date'].to_list(), date)

    if (nearest_date == 0): return 0

    print(account_trans[account_trans['date'] == nearest_date]['date'])

    return 0

print(loan_df.head())
print()
databse = loan_df.apply(get_balance_at_date, axis=1)
