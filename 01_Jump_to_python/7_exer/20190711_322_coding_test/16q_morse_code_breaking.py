# Morse code_breaking _++++++++++++++++ sungmin's one_point_lesson (dictionary로 세팅, 키입력, value출력)
#.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
# ' ': ' ',

dic = { '': ' ','.-':'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',\
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',\
        '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

morse = input("모르스 부호를 입력하세요: ")
print(morse)
morse = morse.split(' ')
print(morse)

for key in morse:
    print(dic[key], end='')

# print("=== 답지 내용 ======")
#
# def morse(src):
#     result = []
#     for word in src.split("  "):
#         for char in word.split(" "):
#             result.append(dic[char])
#         result.append(" ")
#     return "".join(result)
#
# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')