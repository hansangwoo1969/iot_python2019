from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET

tree = parse("1_students_info2.xml")
students_list = tree.getroot()

# def show_individual_detail(node):
print("\n%s (%s)\n\t-성별: %s\n\t-나이: %s\n\t-전공: %s\n\t사용 가능한 언어"
      % (node.get("name"), node.get("ID"), node.get("sex"), node.findtext("age"), node.findtext("major")), end="")
try:
    if node.find('practicable_computer_languages').text:
        for languages in node.find('practicable_computer_languages'):
            print("\n\t\t->%s\t(학습기간: %s, Level: %s)"
                  % (languages.get("name"), languages.find('period').get("value")
                     , languages.get("level")), end="")
    else:
        print(": 없음")
except AttributeError:
    print(": 없음")


def optional_printer(option, keyword):
    tree = parse("students_info2.xml")
    note = tree.getroot()
    option_dict = {1: "ID", 2: "name", 3: "age", 4: "major", 5: "name", 6: "value", 7: "level"}
    node_list_name = []
    for student in note.getiterator("student"):
        if option in range(1, 3):
            if keyword in student.get(option_dict[option]):
                node_list_name.append(student)
        elif option in range(3, 5):
            if keyword in student.find(option_dict[option]).text:
                node_list_name.append(student)
        elif option == 5 or option == 7:
            for language in student.find("practicable_computer_languages"):
                if keyword in language.get(option_dict[option]):
                    node_list_name.append(student)
                    break
        elif option == 6:
            for language in student.find("practicable_computer_languages"):
                if keyword in language.find("period").get(option_dict[option]):
                    node_list_name.append(student)
                    break
    if len(node_list_name) == 1:
        show_individual_detail(node_list_name[0])
    else:
        for std_node in node_list_name:
            print("%s (%s %s %s)" %
                  (std_node.get("ID"), std_node.get("name"), std_node.get("sex"), std_node.find("age").text))

