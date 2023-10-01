import re

SQL_command = "UPDATE USER SET PHONE = newPhone WHERE USERNAME = 'user'"


def fill_command_by_inserts(sql, u, p):
    sql = sql.replace("user", u)
    sql = sql.replace("newPhone", p)
    return sql


def check_phone(p):
    regex_rule = r'^[0-9]{9}$'
    if re.match(regex_rule, p):
        return True
    else:
        return False


try:
    username = input("Zadej svoje jmeno: ")
    phone = input("Zadej svuj telefon: ")
    if check_phone(phone):
        print(fill_command_by_inserts(SQL_command, username, phone))
    else:
        raise Exception("Spatne zadany telefon!")
except Exception as e:
    print(e)
