#product是一个包
import dbutils.sqlite
name = '饮料'
def  print_db():
    return dbutils.sqlite.db_url
#print_db()