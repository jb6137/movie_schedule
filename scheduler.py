import sys
from time_selector import schedule


def main():
    if len(sys.argv) != 3:
        print("Usage: python scheduler.py [filename] [MT/FS]")
        exit(-1)

    filename = sys.argv[1]
    day_of_week = sys.argv[2]

    # read file
    movie_schedules = schedule_movies(filename, day_of_week)
    display_schedules(movie_schedules)


def schedule_movies(filename: str, day_of_week: str) -> list:
    with open(filename) as file:
        schedules = []
        for line in file.read():
            schedules.append(schedule(line, day_of_week))


def display_schedules(movie_schedules: list):
    for movie in movie_schedules:
        print(movie)


if __name__ == '__main__':
    main()
