import json

class Book:
    def __init__(self):
        #Common attributes
        self.title = ''
        self.author = ''
        self.publish_date = ''
        self.page_count = ''
        self.cover_image = ''
        self.isbn = ''
        #Open Library attributes
        self.open_url = ''
        self.subjects = []
        self.notes = ''
        #NY Times attributes
        self.times_desc = ''
        self.amazon_url = ''
        #Google Books attributes
        self.google_id = ''
        self.google_desc = ''
        self.main_category = ''
        self.google_cats = []
        self.google_rating = -1
        self.language = ''

    def fill_open_library(self, open_info):
        if open_info == {}:
            return
        self.open_url = open_info['url']
        if not self.title:
            self.title = str(open_info['title'])
        if not self.isbn:
            self.title = open_info['isbn']
        if not self.publish_date and 'publish_date' in open_info:
            self.publish_date = open_info['publish_date']
        if not self.page_count and 'number_of_pages' in open_info:
            self.title = open_info['number_of_pages']
        if not self.author and 'authors' in open_info:
            joint_author = ''
            for a in open_info['authors']:
                joint_author = joint_author + ", " + a['name']
            self.author = joint_author
        if not self.cover_image and 'cover' in open_info:
            if 'large' in open_info['cover']:
                self.cover_image = open_info['cover']['large']
            elif 'medium' in open_info['cover']:
                self.cover_image = open_info['cover']['medium']
        if 'notes' in open_info:
            self.notes = open_info['notes']
        if 'subjects' in open_info:
            self.subjects = open_info['subjects']
            for i in range(len(self.subjects)):
                self.subjects[i] = self.subjects[i]['name'].lower();


    def fill_ny_times(self, times_info):
        self.isbn = str(times_info['isbn'])
        self.title = times_info['title']
        self.author = times_info['author']
        self.times_desc = times_info['description']
        self.amazon_url = times_info['url']

    def fill_google_books(self, google_info):
        if google_info == {}:
            return
        if 'id' in google_info:
            self.google_id = google_info['id']
        if not self.title:
            self.title = str(google_info['volumeInfo']['title'])
        if not self.author and 'authors' in google_info['volumeInfo']:
            joint_author = ''
            for a in google_info['volumeInfo']['authors']:
                joint_author = joint_author + ", " + a
            self.author = joint_author
        if not self.publish_date and 'publishedDate' in google_info:
            self.publish_date = google_info['publishedDate']
        if not self.isbn and 'industryIdentifiers' in google_info:
            for identifier in google_info['industryIdentifiers']:
                if identifier['type'] == 'ISBN_10':
                    self.isbn = identifier['identifier']
        if not self.page_count and 'pageCount' in google_info:
            self.page_count = google_info['pageCount']
        if 'averageRating' in google_info:
            self.google_rating = google_info['averageRating']
        if 'language' in google_info:
            self.language = google_info['language']
        if 'mainCategory' in google_info:
            self.main_category = google_info['mainCategory']
        if 'categories' in google_info:
            self.google_cats = google_info['categories']
        if 'description' in google_info:
            self.google_desc = google_info['description']
        if not self.cover_image and 'imageLinks' in google_info:
            if 'large' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['large']
            elif 'extraLarge' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['extraLarge']
            elif 'medium' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['medium']

    def getAsDict(self):
        dataDict = {}
        dataDict['title'] = self.title
        dataDict['author'] = self.author
        dataDict['publish_data'] = self.publish_date
        dataDict['page_count'] = self.page_count
        dataDict['cover_image'] = self.cover_image
        dataDict['isbn'] = self.isbn
        dataDict['open_url'] = self.open_url
        dataDict['subjects'] = self.subjects
        dataDict['notes'] = self.notes
        dataDict['times_desc'] = self.times_desc
        dataDict['amazon_url'] = self.amazon_url
        dataDict['google_id'] = self.google_id
        dataDict['google_desc'] = self.google_desc
        dataDict['main_category'] = self.main_category
        dataDict['google_cats'] = self.google_cats
        dataDict['google_rating'] = self.google_rating
        dataDict['language'] = self.language
        return dataDict

    def fillFromDict(self, bookDict):
        self.title = bookDict['title']
        self.author = bookDict['author']
        self.publish_date = bookDict['publish_data']
        self.page_count = bookDict['page_count']
        self.cover_image = bookDict['cover_image']
        self.isbn = str(bookDict['isbn'])
        self.open_url = bookDict['open_url']
        self.subjects = bookDict['subjects']
        self.notes = bookDict['notes']
        self.times_desc = bookDict['times_desc']
        self.amazon_url = bookDict['amazon_url']
        self.google_id = bookDict['google_id']
        self.google_desc = bookDict['google_desc']
        self.main_category =bookDict['main_category']
        self.google_cats =  bookDict['google_cats']
        self.google_rating = bookDict['google_rating']
        self.language = bookDict['language']
