from articles import articles
from typing_classes import TypeSpeedTrainer

articles = articles[0]

print(len(articles))

tst = TypeSpeedTrainer()

def diff_letters(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


def written_text_to_csv(self, text):
    with open(self.file_name, "a") as written_text:
        written_text.write(text)


def diff_letters( a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


def compare_to_input():
    string, string_count = tst.read_written_txt()
    compare_string_article = articles[0:string_count]
    print(f"Error letters: {diff_letters(string, compare_string_article)}")
    print(string, "\n", string_count, "\n", compare_string_article)
    if string == compare_string_article:
        print(True)
    else:
        print(False)
        
compare_to_input()


def read_written_txt():
    file_name = "txt/written_text.txt"
    with open(file_name, "r") as written_text:
        text = written_text.read()
        print(text)
        written_text_count = len(text)
        print(written_text_count)
    return written_text_count

# read_written_txt()
