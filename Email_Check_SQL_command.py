import re

SQL_command = "UPDATE USER SET EMAIL = newEmail WHERE USERNAME = 'user'"


def fill_command_by_inserts(sql, u, em):
    sql = sql.replace("user", u)
    sql = sql.replace("newEmail", em)
    return sql


def check_email(em):
    regex_rule = r'^[a-zA-Z0-9]+.+\@[a-zA-Z]+\.(com|cz)$'
    if re.match(regex_rule, em):
        return True
    else:
        return False


try:
    username = input("Zadej svoje jmeno: ")
    email = input("Zadej svuj email: ")
    if check_email(email):
        print(fill_command_by_inserts(SQL_command, username, email))
    else:
        raise Exception("Spatne zadany email!")
except Exception as e:
    print(e)
