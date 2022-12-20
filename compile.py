class Compile: 
    def __init__(self, users): 
        self.users = users 
        self.id_list = []
        
    def get_ids(self): 
        with open(self.users, 'r') as f: 
            text_file = f.read().split("\n")
            for line in text_file: 
                self.id_list.append(line)

        return self.id_list






