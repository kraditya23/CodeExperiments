# In this module i have tried to recreate the Ordinal Encoding and One Hot
# Encoding using basic python libraries only.

import pandas as pd
import numpy as np


#ORDINAL ENCODING
def ordinal_encoder(df) :
    encoded_dict = {}
    for col in range(len(df.columns)):
        cur_encoded_col = np.empty(len(df), dtype=int)
        my_list = df.iloc[:, col].drop_duplicates().to_numpy()
        for i in range(len(df)):
            cur_encoded_col[i] = np.argwhere(my_list == df.iloc[:, col][i])[0][0]

        encoded_dict[df.columns[col]] = cur_encoded_col

    return pd.DataFrame(encoded_dict)


#ONE HOT ENCODING
def one_hot_encoder(df):
    encoded_dict = {}
    for col in range(len(df.columns)):
        my_list = df.iloc[:, col].drop_duplicates().to_numpy()
        cur_encoded_col = np.zeros((len(my_list), len(df)), dtype=int)
        for i in range(len(df)):
            cur_encoded_col[np.argwhere(my_list == df.iloc[:, col][i])[0][0]][i] = 1

        for i in range(len(my_list)):
            encoded_dict[my_list[i]] = cur_encoded_col[i]

    return pd.DataFrame(encoded_dict)

