SQL_command = ("CREATE TABLE PRISPEVEK (ID INT NOT NULL AUTO_INCREMENT,AUTHOR VARCHAR(100) NOT NULL,TEXT TINYTEXT NOT "
               "NULL,PRIMARY KEY (ID));")


def fill_command_by_inserts(sql, n, t):
    sql = sql.replace("AUTHOR", n)
    sql = sql.replace("TEXT", t, 1)
    return sql


try:
    nickname = input("Zadej svoji presdivku: ")
    text = input("Zadej libovolny text: ")
    print(fill_command_by_inserts(SQL_command, nickname, text))
except Exception as e:
    print(e)
