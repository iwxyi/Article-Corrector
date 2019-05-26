import pycorrector


def save_text_file(file_name, contents):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(contents)


in_str = open("in.txt", "r", encoding="utf-8").read()
corrected_sent, detail = pycorrector.correct(in_str)
save_text_file("out.txt", corrected_sent)
print(detail)
