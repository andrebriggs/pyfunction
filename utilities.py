import json

def getUrls():
    data = {}    
    urls =  ['https://csehackstorage.blob.core.windows.net/image-to-tag/image1.jpeg']
    data['urls'] = urls
    data['count'] = 1
    json_data = json.dumps(data)
    return json_data

def main():
    print(getUrls())

if __name__ == "__main__":
    main()