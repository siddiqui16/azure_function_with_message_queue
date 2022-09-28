import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    name = name if name else "indirect"
    count = req.params.get('count')
    count = int(count) if count else 5

    responses = []
    remote_req_url = "/".join(req.url.split("/")[:-1] + ["HttpTrigger2"])
    
    logging.info(f'Calling "{remote_req_url}" {count} times')
    for i in range(count):
        responses += [requests.post(f"{remote_req_url}?name={name}&count={count*1000+i}")]

    return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")