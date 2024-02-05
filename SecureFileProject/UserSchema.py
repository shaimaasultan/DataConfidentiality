
"""
    def HideFullColumn(user, colNames):
        if colNames in x[user]['names']:
            return "HideFullColumn"
    
    def formattedMask(col1, mask_format):
        masked_positions: list[int] = [i for i, val in enumerate(mask_format) if val == "X"]
        return ''.join(['X' if i in masked_positions else val for i, val in enumerate(col1)])
        
    def HideValue(col, value):
    if col in value:
        return 'HideValue'
    else:
        return col
        
    
    #def HideByCol(user, col1, col2, data, mask_text):
    #    data.loc[:, col1][data[data.loc[:, col2].isin(d.get(user)[0])].index.values] = mask_text


    #d = dict(USER1=[['Val1', '23', '2023-12-01', '300.0']], USER2=[['Val2', 'Val1']])
    
    
    ,
                  #Converter={
            #'Col1': lambda col1: HideValue(col1, ['abc', 'cdf']),
            #'Col2': lambda col2: HideColumnExcept('USER2', 'Col2', col2, d.get('USER2')[0])
                  #  }
    
    ,
                  #Converter={
            #'Col1': lambda Col1: HideValue(Col1, ['abc']),
            #'Col2': lambda Col2: HideColumnExcept('USER1', 'Col2', Col2, d.get('USER1')[0])
            #'Col4': lambda Col4: formattedMask(Col4, "__XXXXX____"),
            #'Col6': lambda Col6: HideFullColumn('USER1', 'Col6'),
        #}

    def HideColumnExcept(user, columnName, col, values):
    if columnName not in x[user]['names'] or col in values:
        return col
    else:
        return 'HideFullColumnExcept'

"""


x = {
    'USER1': dict(names=['Col6', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5'],
                  use_cols=[0, 1, 2, 3, 4, 5],
                  ColDataType=dict(Col6="string",
                                   Col1='string',
                                   Col2='string',
                                   Col3='string',
                                   Col4='string',
                                   Col5="string"),
                  HideFullColumn=['Col6'],
                  HideValue=dict(Col1=['abc', 'cdf'],
                                 Col3=['lana']),
                  HideExceptValue=dict(Col2=['Val1', '23', '2023-12-01', '300.0', '79261', '85850', '90743']),
                  DynamicHideTerms=['Val2', '77', '555663534', '2012.06', '2011.06'],
                  MaskCols=dict(Col3='Col2', Col5='Col1', Col4='Col6')
                  ),
    'USER2': dict(names=['Col6', 'Col1', 'Col2', 'Col3'],
                  use_cols=[0, 1, 2, 3],
                  ColDataType=dict(Col6="string", Col1='string', Col2='string', Col3='string'),
                  MaskCols=dict(Col3='Col2'),
                  HideFullColumn=[],
                  DynamicHideTerms=[],
                  HideExceptValue=dict(Col2=['Val2', 'Val1']),
                  HideValue=dict()
                  ),
    'USER3': dict(names=['Col6', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5'],
                  use_cols=[0, 1, 2, 3, 4, 5],
                  ColDataType=dict(Col6="string",
                                   Col1='string',
                                   Col2='string',
                                   Col3='string',
                                   Col4="string",
                                   Col5="string"),
                  MaskCols=dict(),
                  HideFullColumn=[],
                  DynamicHideTerms=[],
                  HideExceptValue=dict(),
                  HideValue=dict()
                  )
}
