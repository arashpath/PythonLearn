#!/usr/bin/env python
def printList(the_list,level=''):
    for each_item in the_list:
        if isinstance(each_item, list):
            printList(each_item,level+'['+str(the_list.index(each_item))+']')
        else:
            print level+'['+str(the_list.index(each_item))+']: '+each_item

MyList = [
    ['2016',
    [
        ['CLS','E:\FSSAI-DOCS\FLRS\CLS2016'],
        ['SLS','E:\FSSAI-DOCS\FLRS\SLS2016'],
        ['REG','E:\FSSAI-DOCS\FLRS\REG2016']
    ]],
    ['2015',
    [
        ['CLS','E:\FSSAI-DOCS\FLRS\CLS\\2015'],
        ['SLS','E:\FSSAI-DOCS\FLRS\SLS'],
        ['REG','E:\FSSAI-DOCS\FLRS\REG\\2015']
    ]]
]

printList(MyList)