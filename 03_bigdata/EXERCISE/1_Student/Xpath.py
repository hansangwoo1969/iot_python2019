# XPath는 XML을 통해 탐색할 수 있도록 하는 구문, SQL은 데이터 베이스를 검색하는 데 사용, find, findall모두 지원

from xml.etree.ElementTree import Element, parse
import xml.etree.cElementTree as ET

tree =ET.parse('sample.xml')
tree.findall('Books/Book')


# 삭제
element = tree.find("Books/Book[2]")
remove(element)





# 제목으로 책 검색
print(tree.find("Books/Book[Title = 'The Colour of Magic']"))
print(tree.findall("Books/Book/Title")[1].text)

# id = 5인 책 검색
print(tree.find("Books/Book[@id='5']"))  # searches with xml attributes must have '@' before the name

# 두번째 책 검색
print(tree.find("Books/Book[2]"))    # indexes starts at 1, not 0

# 마지막 책 검색
print("# 1 : ", tree.find("Books/book[last()]"))  # 'last' is the only xpath function allowed in ElementTree

# 모든 저자 검색
tree.findall(".//Author")     #searches with // must use a relative path
print("# 2 : ", tree.findall(".//Author")[0].text)