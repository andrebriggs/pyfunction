import logging
import json
import utilities
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
        images = utilities.getImageDictionary(int(imageCount))
        json_data = json.dumps(images)
        return func.HttpResponse(json_data)
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
