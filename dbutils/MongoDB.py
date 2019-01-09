import dbutils.sqlite  #绝对导入
from . import sqlite   #相对导入，.表示当前位置导入全部的sqlite
from .sqlite import db_url #相对导入，只能使用在from里面，表示导入模块下的一个内容