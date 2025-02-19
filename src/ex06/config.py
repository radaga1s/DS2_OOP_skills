import logging

num_of_steps = 3
text_ptrn = ("We have made {length} observations from tossing a coin: " 
            "{tails} of them were tails and {heads} of them were heads. "
            "The probabilities are {tails_prcnt:.2f}% and {heads_prcnt:.2f}%, respectively. "
            "Our forecast is that in the next {steps} observations we will have: "
            "{rnd_tails} tail{end_tail} and {rnd_heads} head{end_head}.")
report_file_name = 'report'
report_file_ext = 'txt'
log_format = '%(asctime)s %(message)s'
log_file = 'analytics.log'
logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    filename=log_file,
                    filemode='w')
logger = logging.getLogger('s21_logger')
ind_err = 'The file path was not passed in arguments'
not_found_err = 'The file was not found'
tg_message_err = '“The report hasn’t been created due to an error”'
tg_message_ok = '“The report has been successfully created”'
url = f'https://api.telegram.org/bot7637269857:AAFdoEgey-euyCs6qAOEyTTYdNItp_TeZ6k/sendMessage'
params = {'chat_id': -1002298687212, 'text': tg_message_err}
