from xml.etree.ElementTree import Element, dump, SubElement, ElementTree

def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail=i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not  elem.tail.strip()):
            elem.tail = i

note = Element('note')

to = Element('to')  #자식노드
to.text = 'Tove'    # 현재 엘리먼트에 값 추가
note.append(to)     # 부모 노드에 자식 노드 추가

SubElement(note, "from").text = "Jani"  # SubElement를 활용하여 자식 노드 추가

indent(note)

dummy = Element("dummy")
note.insert(1, dummy)
dump(note)
note.remove(dummy)  # 부모 노드에 있는 자식 노드를 인자로 넘겨줘야 한다.

note.attrib["date"]="20120124"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend"

indent(note)

dump(note)

ElementTree(note).write("note.xml")
