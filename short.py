class URL_Shortener:
    id = 0
    url2id = {}
    
    def shorten_url(self, original_url, _id):
        self.url2id = {}
        self.id = _id
        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten_url = self.encode(id)
        else:
            self.url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1
        
        return shorten_url
    
    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        return "".join(ret[::-1])
