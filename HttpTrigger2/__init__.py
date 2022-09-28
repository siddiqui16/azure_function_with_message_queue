import logging
import datetime
import azure.functions as func


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage], msg_out: func.Out[func.QueueMessage]) -> func.HttpResponse:
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

    txt = f"{name} {count} is pushing into queue @ {datetime.datetime.utcnow()}"
    msg.set(txt)
    msg_out.set(txt)
    
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
