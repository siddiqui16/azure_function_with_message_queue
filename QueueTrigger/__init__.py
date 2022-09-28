import logging
import time
import random
import azure.functions as func


def main(msg: func.QueueMessage) -> None:
    logging.info('Python queue trigger function processed a queue item: %s', 
                 msg.get_body().decode('utf-8'))
    prod_a = []
    for i in range(random.randint(1,100)):
        prod_a += [i*i]
    res = sum(prod_a) 
    logging.info(f'Result = {res}')
    time.sleep(5)
