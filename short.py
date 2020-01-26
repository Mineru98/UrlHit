class URL_Shortener:
    id = 1
    url2id = {}
    
    def shorten_url(self, original_url):
        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten_url = self.encode(id)
        else:
            self.url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1
        
        return "https://www.urlhit.shop/"+shorten_url
    
    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        return "".join(ret[::-1])

shortener = URL_Shortener()
print(shortener.shorten_url("goooooooooooooogle.com"))
print(shortener.shorten_url("goooooooooooooogle.com"))
print(shortener.shorten_url("veryloooooooongurl.com"))
print(shortener.shorten_url("helllloooooooooooo.com"))
print(shortener.shorten_url("https://coding_interview.com/questions/183658/replacing-letters-with-number"))