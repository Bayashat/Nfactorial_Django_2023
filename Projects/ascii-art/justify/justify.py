import shutil


def print_ascii_art(terminal_width, padding, align, result_art):
    if align == "center":
        padding //= 2
        for line in result_art:
            print(" " * padding + line)
    elif align == "right":
        for line in result_art:
            print(" " * padding + line)
    elif align == 'left':
        for line in result_art:
            print(line)
    elif align == 'justify':
        for line in result_art:
            print(line)
    print(terminal_width * '*')
        
def write_justify_space(text: str, pure_width: int, result_line: str, index: int) -> str:
    """Print extra spaces for justify align

    Args:
        text (str): Input text
        pure_width (int): Ascii art width of all characters in text
        result_line (str): Container str for saving ascii art line
        index (int): index of text

    Returns:
       str: Result str with extra spaces for justify
    """
    words_of_text = text.split(" ")
    last_word = words_of_text[-1]
    terminal_width = shutil.get_terminal_size().columns
    total_empty_spaces = terminal_width - pure_width
    space_between_words = len(words_of_text)-1
    padding = total_empty_spaces // space_between_words
    remainder_in_calc =  total_empty_spaces - padding * space_between_words
    if text[index+1] == last_word[0]: # add remainder padding to last empty space
        padding += remainder_in_calc
    # print(padding, terminal_width, pure_width)
    result_line += (" " * int(padding))
    return result_line