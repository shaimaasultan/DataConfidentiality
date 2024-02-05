import GroupPolicy
import copy

users_list = ['USER1', 'USER2', 'USER3', 'USER4', 'USER5', 'USER6', 'USER7', 'USER8','USER9']

"""initiate all users configurations to an empty configuration"""


def init():
    for user in users_list:
        GroupPolicy.ReadConfig[user] = copy.deepcopy(GroupPolicy.UserInit)


def Config():
    """initiate users configurations"""
    init()

    """ Set Users Data set column names and view columns short list"""
    GroupPolicy.set_DataSetColumnNames(['USER1', 'USER2' , 'USER9'], {0: 'Col0',
                                                            1: 'Col1', 2: 'Col2', 3: 'Col3', 4: 'Col4', 5: 'Col5'})
    GroupPolicy.set_DataSetColumnNames(['USER3'], {0: 'Col0', 1: 'Col1',
                                                   2: 'Col2', 3: 'Col3'})
    GroupPolicy.set_DataSetColumnNames(['USER4'], {1: 'Col1', 2: 'Col2'})
    GroupPolicy.set_DataSetColumnNames(['USER5'], {1: 'Col1', 3: 'Col3'})
    GroupPolicy.set_DataSetColumnNames(['USER6', 'USER7'], {0: 'Col0', 3: 'Col3'})
    GroupPolicy.set_DataSetColumnNames(['USER8'], {2: 'Col2', 3: 'Col3'})

    """Set user configuration to hide Full columns"""
    GroupPolicy.set_HideFullColumn(['USER1', 'USER6', 'USER7', 'USER8'], ['Col0'])

    """Set User configurations by values to be searched in other columns"""
    GroupPolicy.set_HideDynamicTerms(['USER1', 'USER2'],
                                     ['Val2', '77', '555663534' , '300.0' ,'abc' , 'cdf', '2012.06', '2011.06'])
    """Set User configuration to hide column value based on other column value """
    GroupPolicy.set_DynamicColumnsSearch(['USER1'], dict(Col3='Col2'))
    GroupPolicy.set_DynamicColumnsSearch(['USER2'], dict(Col3='Col2', Col5='Col1', Col4='Col0'))

    """Set User configuration to hide column specific value based on list of values for each column"""
    GroupPolicy.set_HideValue(['USER1'], dict(Col1=['abc', 'cdf'], Col3=['lana', 'kana']))
    GroupPolicy.set_HideValue(['USER3'], dict(Col3=['lulu']))

    """Set User configuration to hide column values except values in the list"""
    GroupPolicy.set_HideExceptValue(['USER1', 'USER8'],
                                    dict(Col2=['Val1', '23', '2023-12-01', '300.0', '79261', '85850', '90743']))
    
    """Set User Mask Pattern """
    GroupPolicy.set_MaskPattern(['USER2'] , dict(Col4=['...XXX..XX','X']))
