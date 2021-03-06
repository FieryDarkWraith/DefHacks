import json, time, main, book

#Entry format for SavedBook, LikedBook, DislikedBook lists:
#[[isbn, date], [isbn2, date2], ...]
#So an array of subarrays, where each subarray contains an isbn identifier, and the date it was added to this list

def addSavedBook(username, isbn):
    with open('userdata.json') as f:
        data = json.load(f)
    data[username]['savedBooks'].append(isbn)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getSavedBookList(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    return data[username]['savedBooks']


def addDislikedBook(username, isbn):
    with open('userdata.json') as f:
        data = json.load(f)
    data[username]['dislikedBooks'].append(isbn)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getDislikedBookList(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    return data[username]['dislikedBooks']


def addLikedBook(username, isbn):
    with open('userdata.json') as f:
        data = json.load(f)
    data[username]['likedBooks'].append(isbn)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getLikedBookList(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    return data[username]['likedBooks']


def addTag(username, key, value):
    with open('userdata.json') as f:
        data = json.load(f)    
    data[username]['tagRanks'][key] = value
    with open('userdata.json', 'w') as f:
        json.dump(data, f)

def getTagDict(username): 
    with open('userdata.json') as f:
        data = json.load(f)   
    return data[username]['tagRanks']

#returns a tag over the threshold, else returns None
def getPopularTag(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    maxPop = 0
    popTag = None
    #NOT BEING USED
    popTagType = ''
    rankedTags = data['username']['tagRanks']
    for key in rankedTags:
        if rankedTags[key][0] > 3 and rankedTags[key][0] > maxPop:
            maxPop = rankedTags[key]
            popTag = key
    return popTag


def getCurrentBook(username):
    with open('userdata.json') as f:
        data = json.load(f)
    if(data[username]['currentBook'] == { }):
        return { };
    retBook = book.Book()
    retBook.fillFromDict(data[username]['currentBook'])
    return retBook;


def changeCurrentBook(username, curBook):
    with open('userdata.json') as f:
        data = json.load(f)    
    data[username]['currentBook'] = curBook.getAsDict();
    with open('userdata.json', 'w') as f:
        json.dump(data, f)

def getNum(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    return data[username]['num']


def changeNum(username, offset):
    with open('userdata.json') as f:
        data = json.load(f)    
    data[username]['num'] = data[username]['num'] + offset
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getP(username):
    with open('userdata.json') as f:
        data = json.load(f)    
    return data[username]["P"]


def setP(username, newP):
    with open('userdata.json') as f:
        data = json.load(f)    
    data[username]["P"] = newP
    with open('userdata.json', 'w') as f:
        json.dump(data, f)
