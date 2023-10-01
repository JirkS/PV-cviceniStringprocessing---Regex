import re


def password_policy_check(u, p):
    regex_rule = (r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W)(?!.*' + re.escape(u) + r').{10,}$')

    if re.match(regex_rule, p):
        return True
    else:
        return False


try:
    username = input("Zadej uzivatelske jmeno: ")
    password = input("Zadej heslo: ")
    print(password_policy_check(username, password))
except Exception as e:
    print(e)
