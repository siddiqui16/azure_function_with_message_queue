import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    count = req.params.get('count')
    count = int(count) if count else 5
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    responses = []
    remote_req_url = "/".join(req.url.split("/")[:-1] + ["HttpTrigger2"])
    logging.info(f'Calling "{remote_req_url}" {count} times')
    for i in range(count):
        responses += [requests.post(f"{remote_req_url}?name={name}&count={count}")]


    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
