import pycorrector

corrected_sent, detail = pycorrector.correct('少先队员因该为老人让座')
print(corrected_sent, detail)  # 正确语句，[[原内容，新内容，起始位置，结束位置]]

while True:
    print(pycorrector.correct(input()))
