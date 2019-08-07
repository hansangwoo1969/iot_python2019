from bs4 import BeautifulSoup
html = """
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/1. Basic Concept.nhn?code=158191" title="1987">한국 영화 1987
        </a>
    </div>
</td>
"""
# <a title <= 마우스 타겟시 설명 메세지 출력
soup = BeautifulSoup(html, 'html.parser')  #최상위 노드

print("<soup>")
print(soup)
tag = soup.td
print("\ntag=soup")
print(tag)
tag = soup.div
print("soup.div")
print(tag)

tag = soup.a
print('\ntag=soup.a')
print(tag)

print('\ntag.name')
print(tag.name)

print("\ntag.attrs")   # 해당 태그의 속성
print((tag.attrs))

print('tag.string')  # 해당 태그의 값
print(tag.string)
print(tag.text)

