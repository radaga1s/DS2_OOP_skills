import sys

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
        @staticmethod
        def counts(data: list):
            heads = tails = 0
            for toss in data:
                if toss[0]:
                    heads += 1
                else:
                    tails += 1
            return heads, tails
        
        @staticmethod
        def fractions(result: tuple):
            heads_prcnt = result[0]/sum(result)*100
            tails_prcnt = result[1]/sum(result)*100
            return heads_prcnt, tails_prcnt
        
if __name__ == '__main__':
    try:
        path = sys.argv[1]
        file_lst = Research(path).file_reader()
        cnts = Research.Calculations.counts(file_lst)
        frctns = Research.Calculations.fractions(cnts)
        print(file_lst)
        print(*cnts)
        print(*frctns)
    except IndexError:
        print('The file path was not passed in arguments')
    except FileNotFoundError:
        print('The file was not found')
    except Exception as e:
        print(e)
