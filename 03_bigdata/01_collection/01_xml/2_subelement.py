from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note')

to = Element('to')  #자식노드
to.text = 'Tove'    # 현재 엘리먼트에 값 추가
note.append(to)     # 부모 노드에 자식 노드 추가

dump(note)
dump(to)

SubElement(note, "from").text = "Jani"  # SubEelment를 활용하여 자식 노드 추가
# 아래와 동일한 결과이다
# from_tag = Element("from")
# from_tag.text = "jani"
# note.append("from_tag")

dump(note)