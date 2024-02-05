import copy
from typing import Any
import pandas as pd

"""Users read file configuration dictionary"""
ReadConfig: dict[Any, Any] = dict()

"""Empty user configration"""
UserInit = {'names': [], 'use_cols': [], 'ColDataType': dict(), 'DynamicColumnsSearch': dict(), 'HideFullColumn': [],
            'HideDynamicTerms': [], 'HideALLExceptThisValue': dict() , 'MaskPattern':dict(Col4=['XXXXX_____' ,'.' ]), 'HideValue': dict()}

"""function to Set all users configurations to HideExceptValue """


def set_HideExceptValue(Users_Group_List, dict_condition):
    for user in Users_Group_List:
        ReadConfig[user]['HideALLExceptThisValue'] = dict_condition


"""function to Set all users configurations to DynamicColumnsSearch """


def set_DynamicColumnsSearch(Users_Group_List, dict_condition):
    for user in Users_Group_List:
        ReadConfig[user]['DynamicColumnsSearch'] = dict_condition


"""function to Set all users configurations to HideDynamicTerms """


def set_HideDynamicTerms(Users_Group_List, TermsList):
    for user in Users_Group_List:
        ReadConfig[user]['HideDynamicTerms'] = TermsList


"""function to Set all users configurations to HideFullColumn """


def set_HideFullColumn(Users_Group_List, ColumnNames_List):
    for user in Users_Group_List:
        ReadConfig[user]['HideFullColumn'] = ColumnNames_List


"""function to Set all users configurations to HideValue """


def set_HideValue(Users_Group_List, dict_condition):
    for user in Users_Group_List:
        ReadConfig[user]['HideValue'] = dict_condition


"""function to Set all users Mask pattern configurations """

def set_MaskPattern(Users_Group_List, MaskPattern):
    for user in Users_Group_List:
        ReadConfig[user]['MaskPattern'] = MaskPattern

"""function to Set all users configurations to DataSetColumnNames """


def set_DataSetColumnNames(Users_Group_List: list, dictColumnNamesAndIndex: dict):
    for user in Users_Group_List:
        col_type = dict()
        if user not in ReadConfig.keys():
            """add new user"""
            ReadConfig[user] = copy.deepcopy(UserInit)
        for key, value in dictColumnNamesAndIndex.items():
            col_type[value] = "string"
            ReadConfig.get(user)['names'].append(value)
            ReadConfig.get(user)['use_cols'].append(key)
            ReadConfig.get(user)['ColDataType'] = col_type


"""Read file based on user configurations 
also setting the order of hiding and checking values to make sure all hide configration work correctly"""


def User_Read_csv(user , filepath):
    data = pd.read_csv(
        filepath,
        names=ReadConfig[user]['names'],
        usecols=ReadConfig[user]['use_cols']
    )

    if 'Col1' in data.columns:
        set_HideExceptValue(['USER3', 'USER2'],
                            dict(Col1=[i for i in data['Col1'] if i[:1] == 'c'])
                            )

    data = data.astype(ReadConfig[user]['ColDataType'])

    for key, value in ReadConfig[user]['DynamicColumnsSearch'].items():
        HideByCol(data, user, key, value, 'HideCellDynamic')

    if 'HideALLExceptThisValue' in ReadConfig[user].keys():
        for key, value in ReadConfig[user]['HideALLExceptThisValue'].items():
            HideValueExcept(data, user, key, value, 'HideExceptValue')
    
    for key, value in ReadConfig[user]['MaskPattern'].items():
        MaskExpr(data, user, key,  value[0], value[1])

    for key, value in ReadConfig[user]['HideValue'].items():
        HideValue(data, user, key, value, 'HideValueText')

    HideFullColumn(data, user, ReadConfig[user]['HideFullColumn'], "HideFullColumn")

    #print(data.head(6))
    return data


"""Hide Full Column in data set for user and mask all values by text =[HideFullColumn] """


def HideFullColumn(data, user, colNames, hideText):
    hc = [i for i in colNames if i in ReadConfig[user]['names']]
    data.loc[:, hc] = hideText
    return data


"""mask column values by mask expression="----XXXX---" and mask character="@"""


def MaskExpr(data, user, col, mask_format, MaskCharacter):
    hc = [i for i in ReadConfig[user]['names'] if i == col]
    if len(hc) == 0:
        return
    masked_positions: list[int] = [i for i, val in enumerate(mask_format) if val == "X"]
    for i in data[col].index:
        if data[col][i] == 'HideCellDynamic':
            continue
        data[col][i] = ''.join([MaskCharacter if i in masked_positions else val for i, val in enumerate(data[col][i])])


"""Hide specific values in column by text = [HideValueText]"""


def HideValue(data, user, col, value, HideValueText):
    hc = [i for i in ReadConfig[user]['names'] if i == col]
    if len(hc) == 0:
        return
    data[col][data.isin(value)[col]] = HideValueText


"""Hide all column values except values in list and mask the rest of values by text = [HideExceptValue]"""


def HideValueExcept(data, user, col, value, HideValueText):
    hc = [i for i in ReadConfig[user]['names'] if i == col]
    if len(hc) == 0:
        return
    data[col][~data.isin(value)[col]] = HideValueText


"""Hide one column cell value by other column value but in the same row and hide value by text = [HideCellDynamic]"""


def HideByCol(data, user, col1, col2, mask_text):
    data.loc[:, col1][data[data.loc[:, col2].isin(ReadConfig[user]['HideDynamicTerms'])].index.values] = \
        mask_text
