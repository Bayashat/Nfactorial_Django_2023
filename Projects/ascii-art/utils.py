import argparse, sys

# ANSI color codes
ANSI_COLOR_CODES = {
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
}

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate ASCII art from a given string and banner.")
    parser.add_argument("--output", type=str,
                        help="Output file for the ASCII art.")
    parser.add_argument("--color", type=str,
                        help="Specify the color for the letters.")
    parser.add_argument("--align", type=str, choices=["center", "left", "right",
                        "justify"], default="left", help="Specify the alignment of the ASCII art.")
    parser.add_argument("--reverse", type=str, 
                        help="Get str based on ascii text file")
    
    # Add banner argument conditionally based on reverse
    if "--reverse" not in sys.argv:
        parser.add_argument("text", type=str, help="The input string.")
        parser.add_argument("banner", type=str, nargs='?', default=None, help="The banner style.")
    else:
        pass

    return parser.parse_args()


def load_banner(file_path):
    with open(file_path, 'r') as file:
        return [line.rstrip('\n') for line in file]
    
def total_word_width(start_indexes, align, banner): 
    total = 0
    for j in range(len(start_indexes)):
        char = banner[start_indexes[j]]
        if align == 'justify' and start_indexes[j] == 1: # skip if it is space
            continue
        # print(f'{len(char)}')
        total += len(char)
    # print(f'{total=}')
    return total
