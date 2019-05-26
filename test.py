import pycorrector

corrected_sent, detail = pycorrector.correct('少先队员因该为老人让座')
print(corrected_sent, detail)

while True:
    print(pycorrector.correct(input()))
