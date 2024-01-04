import sys, argparse, shutil, re
from reverse.reverse import reverse_ascii_art, convert_ascii_to_text
from output.output import write_ascii_file
from justify.justify import print_ascii_art, write_justify_space
from color.color import find_colored_letters
from utils import ANSI_COLOR_CODES, parse_arguments, load_banner, total_word_width


    
def main(text, banner, output_file=None, color=None, align="left", reverse=None):
    # Find letters that should be colored if they exist
    color, colored_letters = find_colored_letters(color)

     # Use eval to process escape characters
    processed_text = eval(f'"{text}"')
    # print(processed_text)
    
    text_ascii_codes = [ord(char) for char in processed_text]  # 72, 73

    # start index of each char in text
    start_indexes = list(map(lambda x: 1 + ((x-32) * 9),
                         text_ascii_codes))  # 362, 371

    result_art = []
    
    terminal_width = shutil.get_terminal_size().columns
    # print(terminal_width)
    

    # sum of all char widths(justify: without space, other: with space)
    pure_width = total_word_width(start_indexes, align, banner) 

    # Traverse line by line, search for ascii art
    for i in range(8):
        result_line = ""
        for j in range(len(start_indexes)):
            char = banner[start_indexes[j]]
            if text[j] == "n" and text[j-1] == "\\":
                result_line += " " * (terminal_width)
                continue
            if j != len(text)-1 and text[j] == "\\" and text[j+1] == "n":
                result_line += " " * (terminal_width)
                continue

            # Apply color if specified
            if color and (colored_letters is None or text[j] in colored_letters):
                ansi_color_code = ANSI_COLOR_CODES.get(color, "")
                # Reset color after the character
                char = f"{ansi_color_code}{char}\033[0m"

            # Print extra spaces for justify align
            if align == "justify" and text[j] == " ":
                result_line = write_justify_space(text, pure_width, result_line, j)
            else:
                result_line += char

            start_indexes[j] += 1

        result_art.append(result_line)
    # Print Ascii Art
    if output_file:
        write_ascii_file(output_file, result_art)
    else:
        padding = (terminal_width - pure_width)
        print_ascii_art(terminal_width, padding, align, result_art)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [OPTION] [STRING] [Banner]")
        sys.exit(1)

    args = parse_arguments()

    if args.reverse:
        banner = load_banner('standard.txt')
        reversed_text = reverse_ascii_art(args.reverse, banner)
        # print(reversed_text)
    else:
        # If not provided --reverse param, normally generate Ascii art
        
        # Load the banner
        banner = load_banner(f"{args.banner}.txt") if args.banner != None else load_banner('standard.txt')
        
        words = re.split(r'\\n', args.text)
        print(words)
        for word in words:
            main(word, banner, args.output, args.color, args.align)
