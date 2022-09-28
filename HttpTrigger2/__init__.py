import json
import base64
import logging
import datetime
import azure.functions as func

def get_random_hash():
    d = f"{datetime.datetime.utcnow()}"
    hash_rand = base64.b32encode(d.encode("utf-8")).decode("utf-8") 
    return hash_rand


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage], msgout: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    name = name if name else "direct"
    count = req.params.get('count')
    count = int(count) if count else -1

    blob_file_id = f"{get_random_hash()}.json"
    message_obj = {
        "name": name, 
        "id":count, 
        "timestamp":f"{datetime.datetime.utcnow()}", 
        "blob_file_id": blob_file_id,
        "api_url": "/".join(req.url.split("/"))
    }
    msg.set(json.dumps(message_obj))
    msgout.set(json.dumps(message_obj))
    
    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")