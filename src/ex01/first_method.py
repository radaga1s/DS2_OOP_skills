class Research:
    @classmethod
    def file_reader(cls):
        with open('../data.csv', 'r') as f:
            return f.read()
        
if __name__ == '__main__':
    print(Research.file_reader())
