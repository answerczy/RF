"""
from importlib import reload
reload(product)    重新载入模块 只能作用于import，不能作用from..import
"""
category ='饮料'
tags= ['饮料','碳酸']

def  get_product_list():
    print('All product list...')

def get_produt_list_with_best_sales():
    print('Best sales...')

def add_product():
    print('Add product...')