# This is a sample Python script.
import pandas as pd
import GroupPolicy
import GenerateUsers



if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', None)

    GenerateUsers.Config()
    filepath = 'C:\VSCODE\pycharm\SecureFileProject\data.csv'
    print(filepath)
    for userName in GenerateUsers.users_list:
        GroupPolicy.User_Read_csv(userName , filepath)
