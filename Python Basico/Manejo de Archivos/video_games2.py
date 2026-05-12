import csv

def write_video_games_to_csv(filename, video_games):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'genero', 'desarrollador', 'clasificacion'])
        writer.writeheader()
        for game in video_games:
            writer.writerow(game)

def main():
    video_games = []
    while True:
        nombre = input("inserte el nombre del juego (o 'exit' para parar): ")
        if nombre.lower() == 'exit':
            break
        genero = input("inserte el género del juego: ")
        desarrollador = input("inserte el desarrollador del juego: ")
        clasificacion = input("inserte la clasificación del juego: ")
        video_games.append({
            'nombre': nombre,
            'genero': genero,
            'desarrollador': desarrollador,
            'clasificacion': clasificacion
        })
    write_video_games_to_csv('video_games.csv', video_games)

    print("Nombre\tGénero\tDesarrollador\tClasificación")
    for game in video_games:
        print(f"{game['nombre']}\t{game['genero']}\t{game['desarrollador']}\t{game['clasificacion']}")

if __name__ == "__main__":
    main()


