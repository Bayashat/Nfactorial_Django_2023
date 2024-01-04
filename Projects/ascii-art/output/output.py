def write_ascii_file(output_file, result_art):
    with open(output_file, "a") as file:
                for line in result_art:
                    file.write(line + "\n")