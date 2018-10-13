import sys

def getMockDataProvider(numberOfElements):
        urls =  [
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image1.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image2.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image3.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image4.jpeg',
            'https://csehackstorage.blob.core.windows.net/image-to-tag/image5.jpeg'
        ]
        return urls[:numberOfElements]

def getImageDictionary(count):
    data = {}    
    data['urls'] = getMockDataProvider(count)
    data['count'] = len(data['urls'])
    return data

def main(count):
    print(getImageDictionary(count))

if __name__ == "__main__":
    main(int(sys.argv[1]))