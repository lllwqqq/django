#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/27 下午3:43
@Author:  Aroma
@File: qytang.py
@Software: PyCharm
"""


class StrTest:
    dep1 = 'Security'
    dep2 = 'Python'
    manager1 = 'cq_bomb'
    manager2 = 'qin_ke'
    fees1 = 4353.34534534
    fees2 = 53453.3434534
    info1 = ' Department01 name: {0:<10}   Manager: {1:<10}  COURCE FEES: {2:<10.2f} The END! '.format(dep1, manager1,
                                                                                                       fees1)
    info2 = ' Department02 name: {0:<10}   Manager: {1:<10}  COURCE FEES: {2:<10.2f} The END! '.format(dep2, manager2,
                                                                                                       fees2)
    print('=' * 89)
    print(info1)
    print(info2)
    print('=' * 89)


if __name__ == '__main__':
    StrTest()
