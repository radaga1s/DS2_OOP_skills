import sys
from config import *
from analytics import Research
import requests

def main():
    path = sys.argv[1]
    file_lst = Research(path).file_reader()
    rc_instance = Research.Calculations(file_lst)
    cnts = rc_instance.counts()
    frctns = rc_instance.fractions()
    rnd_lst = Research.Analytics(file_lst).predict_random(num_of_steps)
    rnd_cnts = Research.Calculations(rnd_lst).counts()
    res_text = f"{text_ptrn.format(length=len(file_lst), 
        tails=cnts[1], heads=cnts[0], tails_prcnt=frctns[1], heads_prcnt=frctns[0],
        steps=num_of_steps, rnd_tails=rnd_cnts[1], rnd_heads=rnd_cnts[0],
        end_tail = 's' if rnd_cnts[1] != 1 else '',
        end_head = 's' if rnd_cnts[0] != 1 else '')}"
    Research.Analytics.save_file(res_text, report_file_name, report_file_ext)

if __name__ == '__main__':
    try:
        main()
    except IndexError as e:
        logger.error(f'{e} {ind_err}')
        print(ind_err)
    except FileNotFoundError as e:
        logger.error(f'{e} {not_found_err}')
        print(not_found_err)
    except Exception as e:
        logger.error(e)
        print(e)
    else:
        params['text'] = tg_message_ok
    response = requests.post(url, json=params)
