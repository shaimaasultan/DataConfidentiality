"""


ReadConfig = {
    'USER1': dict(names=['Col0', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5'],
                  use_cols=[0, 1, 2, 3, 4, 5],
                  ColDataType=dict(Col0="string",
                                   Col1='string',
                                   Col2='string',
                                   Col3='string',
                                   Col4="string",
                                   Col5="string"),
                  DynamicColumnsSearch=dict(),
                  HideFullColumn=[],
                  HideDynamicTerms=[],
                  HideALLExceptThisValue=dict(),
                  HideValue=dict()
                  ),
    'USER2': dict(names=['Col0', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5'],
                  use_cols=[0, 1, 2, 3, 4, 5],
                  ColDataType=dict(Col0="string",
                                   Col1='string',
                                   Col2='string',
                                   Col3='string',
                                   Col4='string',
                                   Col5="string"),
                  HideFullColumn=['Col0'],
                  HideValue=dict(Col1=['abc', 'cdf'],
                                 Col3=['lana', 'kana']),
                  HideALLExceptThisValue=dict(Col2=['Val1', '23', '2023-12-01', '300.0', '79261', '85850', '90743']),
                  HideDynamicTerms=['Val2', '77', '555663534', '2012.06', '2011.06'],
                  DynamicColumnsSearch=dict(Col3='Col2', Col5='Col1', Col4='Col0')
                  ),
    'USER3': dict(names=['Col0', 'Col1', 'Col2', 'Col3'],
                  use_cols=[0, 1, 2, 3],
                  ColDataType=dict(Col0="string", Col1='string', Col2='string', Col3='string'),
                  DynamicColumnsSearch=dict(Col3='Col2'),
                  HideFullColumn=[],
                  HideDynamicTerms=[],
                  HideALLExceptThisValue=dict(Col2=['Val2', 'Val1']),
                  HideValue=dict()
                  )

}
"""

