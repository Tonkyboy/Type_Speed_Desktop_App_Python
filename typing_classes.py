from time import sleep
from articles import articles

articles = articles[0]

class TypeSpeedTrainer():
    def __init__(self):
        self.file_name = f"txt/written_text.txt"
        self.articles = articles[0]

    def start(self):
        pass

    def restart(self):
        self.clear_written_text()

    def diff_letters(self, a, b):
        return sum(a[i] != b[i] for i in range(len(a)))

    def compare_to_input(self):
        string, string_count = self.read_written_txt()
        compare_string_article = articles[:string_count]
        errors = self.diff_letters(string, compare_string_article)
        # print(f"Error letters: {errors}")
        # print("string: " + str(string), "\n", "string_count: " + str(string_count), "\n", "compare_string_article: " + str(compare_string_article))
        if string == compare_string_article:
            return True, errors, string_count
        else:
            return False, errors, string_count

    def show_score(self):
        pass

    def written_text_to_csv(self, text):
        with open(self.file_name, "a") as written_text:
            written_text.write(text)

    def read_written_txt(self):
        with open(self.file_name, "r") as written_text:
            text = written_text.read()
            # print(text)
            written_text_count = len(text)
            # print(written_text_count)
        return text, written_text_count

    def clear_written_text(self):
        with open(self.file_name, "r+") as written_text:
            written_text.truncate()


