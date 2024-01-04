def find_colored_letters(color: str) -> (str, None or str):
    if color and " " in color:
        color_list = color.split(" ")
        colored_letters = color_list[1]
        color = color_list[0]
        return (color, colored_letters)
    else:
        colored_letters = None
        return (color, colored_letters)
