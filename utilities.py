import sys

def getMockDataProvider(numberOfElements):
        #We expect to have a data access layer that will query and retrieve data from a datastore
        # Mocking for now. We should use dependency injection here  
        mockUrls =  [
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image1.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image2.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image3.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image4.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image5.jpeg'
        ]
        return mockUrls[:numberOfElements]

def getImageDictionary(count):
    data = {}    
    data['urls'] = getMockDataProvider(count)
    data['count'] = len(data['urls'])
    return data

def main(count):
    print(getImageDictionary(count))

if __name__ == "__main__":
    main(int(sys.argv[1]))