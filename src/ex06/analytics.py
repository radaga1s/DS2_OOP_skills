from random import randint
from config import logger

class Research:
    def __init__(self, path):
        logger.info(f'Calling class {__class__.__name__} instance initializer with {path=}')
        self.path = path

    def file_reader(self, has_header=True):
        logger.info(f'Opening file by file_reader() method with arg {has_header=}')
        with open(self.path, 'r') as f:
            if has_header:
                _, *lines = f.readlines()
            else:
                lines = f.readlines()
            return [[int(i) for i in line.split(',')] for line in lines]
        
    class Calculations:
        def __init__(self, data: list):
            logger.info(f'Calling class {__class__.__name__} instance initializer')
            self.data = data
            self.heads = self.tails = 0
            self.heads_prcnt = self.tails_prcnt = 0.0

        def counts(self):
            logger.info('Calculating the counts of heads and tails by calling counts() method')
            for toss in self.data:
                if toss[0]:
                    self.heads += 1
                else:
                    self.tails += 1
            return self.heads, self.tails
        
        def fractions(self):
            logger.info('Calculating the percents of heads and tails by calling fractions() method')
            self.heads_prcnt = self.heads/len(self.data)*100
            self.tails_prcnt = self.tails/len(self.data)*100
            return self.heads_prcnt, self.tails_prcnt

    class Analytics(Calculations):
        def predict_random(self, length: int):
            logger.info('Filling by the percents of heads and tails by calling predict_random() method')
            self.res = []
            for _ in range(length):
                temp = []
                temp.append(randint(0, 1))
                temp.append(0 if temp[0] else 1)
                self.res.append(temp)
            return self.res
        
        def predict_last(self):
            logger.info('Returning the last attempt of coin toss by method predict_last()')
            return self.data[-1]
        
        @staticmethod
        def save_file(text, file_name, ext):
            logger.info(f'Saving file {file_name}.{ext}')
            with open(f'{file_name}.{ext}', 'w') as out:
                out.write(text)

