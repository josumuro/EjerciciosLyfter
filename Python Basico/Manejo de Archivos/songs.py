def songs(path):
    with open(path) as Songs:
        lines = Songs.readlines()
        lines.sort()
        with open('sorted_songs.txt', 'w') as output_file:
            for line in lines:
                output_file.write(f'Cancion: {line}')
songs('songs.txt.txt')

