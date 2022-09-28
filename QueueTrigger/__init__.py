import logging
import time
import random
import azure.functions as func


def main(msg: func.QueueMessage, msgout: func.Out[func.QueueMessage]) -> None:
    msg_content = msg.get_body().decode('utf-8')
    msg_content = msg_content.replace(r'\n','')
    logging.info(f'Python queue trigger function processed a queue item: {msg_content}')
    prod_a = []
    for i in range(random.randint(2,10)):
        prod_a += [i*i]
    res = sum(prod_a)
    res_str =  f"Result = {res:5}: {msg_content}"
    logging.info(res_str)
    msgout.set(res_str)
    time.sleep(15)
