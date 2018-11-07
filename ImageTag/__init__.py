import logging
import json
import azure.functions as func
import os
import pg8000

# Update connection string information obtained from the portal
host = os.environ['DB_HOST']
user = os.environ['DB_USER'] 
dbname = os.environ['DB_NAME']
password = os.environ['DB_PASS']

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
        images = get_untagged_images(int(imageCount))
        json_data = json.dumps(images)
        return func.HttpResponse(json_data)
    else:
        return func.HttpResponse(
             "Please pass imageCount on the query string or in the request body",
             status_code=400
        )

def get_untagged_images(num):
    # Open connection
    conn = pg8000.connect(user, host=host, unix_sock=None, port=5432, database=dbname, password=password, ssl=True, timeout=None, application_name=None)
    cursor = conn.cursor()

    # GET N existing UNTAGGED rows
    selected_images_to_tag = {}
    cursor.execute("SELECT b.ImageId, b.originalimagename, a.TagStateId FROM Image_Tagging_state a JOIN Image_Info b ON a.ImageId = b.ImageId WHERE a.TagStateId = 0 order by a.createddtim DESC limit {0}".format(num))
    for row in cursor:
        print('Image Id: {0} \t\tImage Name: {1} \t\tTag State: {2}'.format(row[0], row[1], row[2]))
        selected_images_to_tag[str(row[0])] = str(row[1])
    '''
    # UPDATE rows from UNTAGGED --> TAG IN PROGRESS
    tag_in_progress = 1
    if(len(selected_images_to_tag) > 0):
        images_to_update = '{0}'.format(', '.join(selected_images_to_tag.keys()))
        cursor.execute("UPDATE Image_Tagging SET TagStateId = {0} WHERE ImageId IN ({1})".format(tag_in_progress,images_to_update))
        conn.commit()
        print(f"Updated {len(selected_images_to_tag)} images to the state {tag_in_progress}")
    else:
        print("No images untagged images left!")
    '''
    return list(selected_images_to_tag.values())