

class TextPreprocessor:
    def __init__(self):
        pass

    def run(self, text):
        raise RuntimeError("Not implemented")


class SimpleTextPreprocessor(TextPreprocessor):
    def __init__(self):
        super().__init__()

    def run(self, text):
        text = text.lower()
        text = text.replace("\n", " ")
        return text
