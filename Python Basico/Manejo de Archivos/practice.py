def open_and_print_file_per_line(path):
    with open(path) as file:
        for line in file:
            print(f'Line: {line.rstrip()}')

open_and_print_file_per_line('c:/ruta/completa/words.txt')