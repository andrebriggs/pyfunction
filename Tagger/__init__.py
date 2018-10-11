import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    imageCount = req.params.get('imageCount')
    if not imageCount:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            imageCount = req_body.get('imageCount')

    if imageCount:
        return func.HttpResponse(f"You requested {imageCount} images!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
