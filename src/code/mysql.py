import sys
import globs
import env
import mysql.connector as _mysql

# Load MYSQL
db = _mysql.connect(host=env.MYSQL_SERVER, user=env.MYSQL_USERNAME, passwd=env.MYSQL_PASSWORD, db=env.MYSQL_DB)


class MysqlClass:
    def insert(self, table, doc):
        for el in doc:
            if isinstance(doc[el], str):
                doc[el] = doc[el].replace('"', '\\"')

        keys = ", ".join(doc.keys())
        values = ", ".join(f'"{w}"' for w in doc.values())

        qry = "INSERT INTO `" + table + "` (" + keys + ") VALUES (" + values + ")"

        cursor = db.cursor()
        cursor.execute(qry)
        db.commit()
        return cursor.lastrowid

    def update(self, table, doc, where=""):
        for el in doc:
            if isinstance(doc[el], str):
                doc[el] = doc[el].replace('"', '\\"')

        if where != "":
            where = " WHERE " + where
        values = ", ".join(["=".join([key, '"' + str(val) + '"']) for key, val in doc.items()])

        qry = "UPDATE " + table + " SET " + values + where

        cursor = db.cursor()
        cursor.execute(qry)
        db.commit()

    def get(self, table, where="", limit=10, select="*"):
        cursor = db.cursor(dictionary=True)
        if where != "":
            where = " WHERE " + where
        sql = """SELECT """ + select + """ FROM """ + table + where + """ LIMIT """ + str(limit)

        res = cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return res
    def get_by_query(self, query):
        cursor = db.cursor(dictionary=True)

        res = cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res
    def get_single_by_query(self, query):
        cursor = db.cursor(dictionary=True)

        res = cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res
        

    def get_single(self, table, where="", select="*"):
        cursor = db.cursor(dictionary=True)
        if where != "":
            where = " WHERE " + where
        query = """SELECT """ + select + """ FROM """ + table + where + """ LIMIT 1"""

        res = cursor.execute(query)
        res = cursor.fetchone()
        cursor.close()
        return res

    def get_count(self, table, where=""):
        cursor = db.cursor(dictionary=True)
        if where != "":
            where = " WHERE " + where
        sql = """SELECT count(*) as total FROM """ + table + where + """ LIMIT 1"""

        res = cursor.execute(sql)
        res = cursor.fetchone()

        cursor.close()
        return res["total"]

    def delete(self, table, where=""):
        cursor = db.cursor(dictionary=True)
        if where == "":
            return False

        sql = """DELETE FROM """ + table + " WHERE " + where

        cursor.execute(sql)
        cursor.fetchone()
        cursor.close()

        return True
