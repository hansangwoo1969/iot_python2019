from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note')

to = Element('to')  #자식노드
to.text = 'Tove'    # 현재 엘리먼트에 값 추가
note.append(to)     # 부모 노드에 자식 노드 추가

dump(note)
dump(to)

SubElement(note, "from").text = "Jani"  # SubElement를 활용하여 자식 노드 추가
dump(note)

note.attrib["date"] = "20120104"   # 노드에 속성 삽입
dump(note)
