
class TimeSelector:
    open = {1: 480 + 60, 2: 630 + 60}
    close = {1: 1380, 2: 1410}

    @staticmethod
    def schedule(line: str, day_of_week: str) -> str:
        # 1. grab name, rating, time from line
        title, year, rating, running_time = parse(line)

    @staticmethod
    def validate_day(day_of_week: str) -> int:
        # M-T: 1 .
        if day_of_week == "MT":
            return 1
        elif day_of_week == "FS":
            return 2

        raise ValueError("Please enter MT or FS for day of week")

    @staticmethod
    def parse(line: str) -> list:
        tokens = line.split(',')
        return tokens[0], tokens[1], tokens[2]

    @staticmethod
    def fit_into_day(name, running_time, day_of_week):
        # 1. first pass, start w end of day, iteratively subtract running time in mins + 35, go until time is less than open time
        # 2. shift times a bit to easy to remember times (multiples of 5). At this point, from 1, there is no spare time, so
        #   we may or may not have to throw out earliest movie. Worst case is number of movies in day *5 = X. if start time of
        # earliest movie to opening time + 60 is greater than X, shift movies starting with latest first. Otherwise, remove earliest
        # movie (and repeat check that N * movies < earliest movie - opening time). Shift by 1-4 mins to get to closest multiple of 5 mins
        # 3. If after shifting, there is enough time in the lowest slot to add a movie, add it
        #

    @staticmethod
    def convert_to_mins(movie_len: str) -> int:
        times = movie_len.split(":")
        hour, mins = int(times[0]), int(times[1])
        # print(f"{movie_len} {times} {hour} {mins}")
        return hour*60 + mins
