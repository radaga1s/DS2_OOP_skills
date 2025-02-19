import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as f:
            if has_header:
                _, *lines = f.readlines()
            else:
                lines = f.readlines()
            return [[int(i) for i in line.split(',')] for line in lines]
        
    class Calculations:
        def __init__(self, data: list):
            self.data = data
            self.heads = self.tails = 0
            self.heads_prcnt = self.tails_prcnt = 0.0

        def counts(self):
            for toss in self.data:
                if toss[0]:
                    self.heads += 1
                else:
                    self.tails += 1
            return self.heads, self.tails
        
        def fractions(self):
            self.heads_prcnt = self.heads/len(self.data)*100
            self.tails_prcnt = self.tails/len(self.data)*100
            return self.heads_prcnt, self.tails_prcnt

    class Analytics(Calculations):
        def predict_random(self, length: int):
            self.res = []
            for _ in range(length):
                temp = []
                temp.append(randint(0, 1))
                temp.append(0 if temp[0] else 1)
                self.res.append(temp)
            return self.res
        
        def predict_last(self):
            return self.data[-1]
        
if __name__ == '__main__':
    try:
        path = sys.argv[1]
        file_lst = Research(path).file_reader()
        instance = Research.Calculations(file_lst)
        cnts = instance.counts()
        frctns = instance.fractions()
        rnd_lst = Research.Analytics(file_lst).predict_random(3)
        last = Research.Analytics(file_lst).predict_last()
        print(file_lst)
        print(*cnts)
        print(*frctns)
        print(rnd_lst)
        print(last)
    except IndexError:
        print('The file path was not passed in arguments')
    except FileNotFoundError:
        print('The file was not found')
    except Exception as e:
        print(e)
