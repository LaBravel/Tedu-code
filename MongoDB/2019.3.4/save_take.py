from pymongo import mongo_client
import bson.binary

img = myset.find_one({'filename':'mm.jpg'})

#写入本地
with open('text.jpg','wb') as f:
    f.write(img(data))