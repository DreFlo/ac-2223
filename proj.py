import pandas as pd



client_df = pd.read_csv('.\\ficheiros_competicao_dev\\client.csv', sep=';')

print(client_df.to_string())

client_df['birthday'] = client_df['birth_number'].apply(lambda bn : str(bn)[0:2] + '-' + str(int(str(bn)[2:4]) % 50) + '-' + str(bn)[4:6])

client_df['male'] = client_df['birth_number'].apply(lambda bn : int(str(bn)[4:6]) >= 51)

print(client_df['male'].unique())

#print(client_df.to_string())

'''

trans_df = pd.read_csv('.\\ficheiros_competicao_dev\\trans_dev.csv', sep=';')

print(trans_df['operation'].unique())

print(trans_df['k_symbol'].unique())

'''

#str(int(str(bn)[2:4]) % 50)