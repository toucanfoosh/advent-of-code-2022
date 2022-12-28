class rps:
    def __init__(self):
        self.won = 6
        self.draw = 3
        self.lost = 0
        self.rock = 1
        self.paper = 2
        self.scissors = 3
        self.score = 0

    def get_points(self, other, mine):
        self.score += self.__get_result(mine)
        self.score += self.__get_choice(mine, other)

    def __get_result(self, mine: str) -> int:
        if (mine == "X"):
            return self.lost
        elif (mine == "Y"):
            return self.draw
        elif (mine == "Z"):
            return self.won

    def __get_choice(self, mine: str, other: str) -> int:
        if (mine == "X"):
            return ((self.__get_choice_helper(other)+1) % 3) + 1
        elif (mine == "Y"):
            return self.__get_choice_helper(other)
        elif (mine == "Z"):
            return (self.__get_choice_helper(other) % 3) + 1

    def __get_choice_helper(self, other: str) -> int:
        if (other == "A"):
            return self.rock
        elif (other == "B"):
            return self.paper
        elif (other == "C"):
            return self.scissors

def main():
    score = rps()
    with open('2/2-dataset.txt', 'r') as fp:
        lines = [line.rstrip() for line in fp]
        for line in lines:
            score.get_points(line[0], line[2])

    print(score.score)


if __name__ == "__main__":
    main()
