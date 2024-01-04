def convert_ascii_to_text(ascii_art: list, banner: str):
    index_of_word_in_text = 0
    # Reversely search the index of the character in the banner and convert it to the corresponding original character
    reversed_text = ""
    for i in range(1):
        reversed_line = ascii_art[i][0]  # first char
        result_of_search = {}
        index = banner.find(reversed_line) 
        print(f"index = {index}")
        for j in range(1, len(ascii_art[i])): # travel line by line
            # find all occurance of given char
            if index != -1:
                reversed_line += ascii_art[i][j]
                # result_of_search.append(index)
            else:
                reversed_line = reversed_line[:-1]
                print(banner.find(reversed_line))
                # index = 0
                # while index != -1:
                #     index = banner.find(reversed_line, index)
                #     if index == -1:
                #         break
                #     result_of_search[index_of_word_in_text] = [].append(index)
                #     print(result_of_search[0])
 
            # # 计算原始字符的 ASCII 码并转换为字符
            # reversed_line += chr((index - 1) // 9 + 32)
    # return reversed_text
    
def reverse_ascii_art(file_path, banner):
    
    with open(file_path, 'r') as file:
        # Read Ascii art file
        ascii_art_lines = [line.rstrip('\n') for line in file]

    # Convert Ascii art text to normal txt
    reversed_text = convert_ascii_to_text(ascii_art_lines, banner)

    return reversed_text
    