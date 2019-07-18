class ChineseCharsNotFound(Exception):
    """
    Raised when no Chinese characters are found in input.

    Args:
        text_input (str): Text input containing no Chinese characters.

    Attributes:
        text_input (str): Text input containing no Chinese characters.
        msg (str): Error message showing the text input.
    """
    def __init__(self, text_input):
        self.text_input = text_input
        self.msg = f'No Chinese characters found in "{self.text_input}"'