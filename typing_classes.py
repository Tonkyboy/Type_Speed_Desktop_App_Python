from time import sleep
# from articles import articles

# articles = articles[0]

class TypeSpeedTrainer():
    def __init__(self):
        self.file_name = f"txt/written_text.txt"
        # self.articles = articles[0]

    def restart(self):
        self.clear_written_text()

    def diff_letters(self, a, b):
        return sum(a[i] != b[i] for i in range(len(a)))

    def compare_to_input(self, articles):
        """ Compares the written text to .txt to the chosen quote """
        string, string_count = self.read_written_txt()
        # compare_string_article = articles[:string_count]
        compare_string_article = articles[:string_count]
        errors = self.diff_letters(string, compare_string_article)
        # print(f"Error letters: {errors}")
        # print("string: " + str(string), "\n", "string_count: " + str(string_count), "\n", "compare_string_article: " + str(compare_string_article))
        if string == compare_string_article:
            return True, errors, string_count
        else:
            return False, errors, string_count

    def written_text_to_csv(self, text):
        """ Writes the input text to a .txt file """
        with open(self.file_name, "a") as written_text:
            written_text.write(text)

    def read_written_txt(self):
        """ Reads the  text from a .txt file """
        with open(self.file_name, "r") as written_text:
            text = written_text.read()
            # print(text)
            written_text_count = len(text)
            # print(written_text_count)
        return text, written_text_count

    def clear_written_text(self):
        """ Clears the .txt file """
        with open(self.file_name, "r+") as written_text:
            written_text.truncate()


