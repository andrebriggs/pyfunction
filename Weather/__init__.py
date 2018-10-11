import logging
import datetime

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(f"The weather is sunny at {datetime.datetime.now()}!")
