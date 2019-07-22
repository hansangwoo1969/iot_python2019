from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET

base = """
학생정보 XML데이터 분석 시작...

1. 요약 정보
2. 전체 데이터 조회
3. 종료
메뉴입력: """

tree = parse('students_info.xml')
note = tree.getroot()
# print(note.tag, note.attrib)   # student_list {}

for child in note:
    # print(child.attrib)
    print(child.tag, child.attrib)
#     for lng in note.iter('language'):
#         if lng:
#             print(lng.tag, lng.attrib)
#     for prd in note.iter('period'):
#         if prd:
#             print(prd.tag, prd.attrib )
# 특정 노드의 전체 속성값 출력
# print("1_특정노드_keys의 전체 속성값 출력")
# for key in note.keys():
#     print(note.get(key))
#
# from_tag = note.find("student")
#
# for key in from_tag.keys():
#     print(from_tag.get(key))





# print("2_모든 자식 노드의 값 접근")
# for parent in tree.getiterator():
#     print(parent.get('name'))
#     print(parent.get('sex'))
#     # for child in parent:
    #     if child ==  None:
    #         continue
    #     print(child.text)
        # for
        # for son in child:
        #     print(son.text)


# #


# def whole_xml():
#     tree = parse("student_info.xml")
#     note = tree.getroot()
#     for parent in note.get.iterator("student"):
#         print("* %s" % parent.get("name"))
#         print("- 성별: %s" % parent.get("sex"))
#         print("- 나이: %s" % parent.findtext("age"))
#         print("- 전공: %s" % parent.findtext("major"))
#         for language_value in parent.getiterator("language"):
#             if language_value:
#                 for period in
#



