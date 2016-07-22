
class Page():
    para = "paragraph"
    options = []
    links = []
    final = False
    
class Book():
    pages = 0
    active_page = 0
    book = []
    def load(self, json_file):
        json_data = open(json_file, 'r')
        book_data = json.load(json_data)
        self.book = []
        for page in book_data:
            new_page = Page()
            new_page.para = page['para']
            new_page.options = page['options']
            new_page.links = []
            for link in page['links']:
                new_page.links.append(int(link))
            if (page['final']=='true' or 
        	        page['final']=='True'):
                new_page.final = True
                #continue
            else:
                new_page.final = False
            self.book.append(new_page)
        json_data.close()
        return self.book
