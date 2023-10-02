import xml.etree.ElementTree as ET
import os

def person_search(xml):
    with open(xml, "r") as file:
        data = file.read()
        return str(data)


try:
    path_xml_file = "data.xml"
    c_d = os.path.dirname(os.path.abspath(__file__))
    f_p = os.path.join(c_d, path_xml_file)
    if os.path.exists(f_p):
        print("huh")

    print(person_search(f_p))
except Exception as e:
    print(e)
