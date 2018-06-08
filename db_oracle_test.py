import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

USER = "deveagle02"
PASSWORD = "deveagle02"
CONNECT_STRING = "rac-scan.lettydomain.com:1521/pengrun"

MAIN_CONNECT_STRING = "%s/%s@%s" % (USER, PASSWORD, CONNECT_STRING)

connectionPool = cx_Oracle.SessionPool(user=USER, password=PASSWORD, dsn=CONNECT_STRING, min=5, max=20, increment=1)

'''
sql分页美化(自行校验参数值的合法性)
    original_sql:原始sql
    current_page:第几页，从1开始
    page_size:每页的条数
    return str
'''
def sql_paging_convert(original_sql,current_page=1,page_size=10):
    start = (current_page-1) * page_size
    end = current_page * page_size
    return "SELECT * FROM (SELECT TMP_TB.*,ROWNUM ROW_ID FROM ({}) TMP_TB WHERE ROWNUM<={}) WHERE ROW_ID>{}".format(original_sql,end,start)

def db_from_row_to_dict(description, record):
    d = {}
    if record is None or description is None:
        return None
    for index in range(len(description)):
        d[description[index][0]] = record[index]
    return d

def execute_dml(update_sql):
    connection = connectionPool.acquire()
    cursor = connection.cursor()
    try:
        cursor.execute(update_sql)
        connection.commit()
        return True
    finally:
        if cursor:
            cursor.close()
        if connection:
            connectionPool.release(connection)
def execute_select(select_sql):
    connection = connectionPool.acquire()
    cursor = connection.cursor()
    try:
        db_results = cursor.execute(select_sql)
        db_table_description = db_results.description
        results = []
        for row in db_results:
            results.append(db_from_row_to_dict(db_table_description, row))
        return results
    finally:
        if not cursor:
            cursor.close()
        if not connection:
            connectionPool.release(connection)

if __name__ == '__main__':
# select_user = 'select USERID,MOBILE from USER_MAIN where userid < 10'
# users_list_dict = execute_select(sql_paging_convert(select_user,3,4))
# print(users_list_dict)
    execute_dml("update  USER_MAIN set EMAIL = '10036@qq.com' where USERID in (109484)")
