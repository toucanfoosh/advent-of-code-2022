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
        self.score += self.__get_result(other, mine)
        self.score += self.__get_choice(mine)

    def __get_result(self, other: str, mine: str) -> int:
        score = 0
        if (other == "A"):
            score += self.__get_result_helper(mine, "Y", "Z", "X")
        elif (other == "B"):
            score += self.__get_result_helper(mine, "Z", "X", "Y")
        elif (other == "C"):
            score += self.__get_result_helper(mine, "X", "Y", "Z")
        return score

    def __get_result_helper(self, other: str, won: str, lost: str, draw: str):
        if (other == won):
            return self.won
        elif (other == lost):
            return self.lost
        elif (other == draw):
            return self.draw
        
    def __get_choice(self, mine):
        out = 0
        
        if (mine == "X"):
            out = self.rock
        elif (mine == "Y"):
            out = self.paper
        elif (mine == "Z"):
            out = self.scissors

        return out

def main():
    score = rps()
    with open('2/2-dataset.txt', 'r') as fp:
        lines = [line.rstrip() for line in fp]
        for line in lines:
            score.get_points(line[0], line[2])
    
    print(score.score)
            
        

if __name__ == "__main__":
    main()