import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        with open(self.path, 'r') as f:
            return f.read()


def file_checker(file_str : str)  -> bool:
    first, *others = file_str.split('\n')
    if first.count(',') != 1 or first.startswith(',') or first.endswith(','):
        return False
    return all(s == '0,1' or s == '1,0' for s in others)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        file_str = Research(path).file_reader()
        if file_checker(file_str):
            print(file_str)
        else:
            raise Exception('The file with a different structure was given')
    except IndexError:
        print('The file path was not passed in arguments')
    except FileNotFoundError:
        print('The file was not found')
    except Exception as e:
        print(e)
