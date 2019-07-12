dic = {'.-':'A',
'-...':'B',
'-.-.':'C',
'-..':'D',
'.':'E',
'..-.':'F',
'--.':'G',
'....':'H',
'..':'I',
'.---':'J',
'-.-':'K',
'.-..':'L',
'--':'M',
'-.':'N',
'---':'O',
'.--.':'P',
'--.-':'Q',
'.-.':'R',
'...':'S',
'-':'T',
'..-':'U',
'...-':'V',
'.--':'W',
'-..-':'X',
'-.--':'Y',
'--..':'Z'}
c = 0
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.-- ////////// H E  S L E E P S  E A R L Y
moss = input('모스부호를 입력하세요: ')
new_moss = moss
moss = moss.split()

for i in moss:
    if i in dic:
        # new_moss = new_moss.replace(i, dic[i])  # replace("찾을 값", "바꿀 값", [바꿀 횟수])
         new_moss = new_moss.replace(i, dic[i], 1)  # replace("찾을 값", "바꿀 값", [바꿀 횟수])
print(new_moss)