import tweepy 
import config 

class Compile: 
    def __init__(self, users, bearer_token): 
        self.users = users 
        self.bearer_token = bearer_token
        self.userdic = {}
        self.user_list = []
        self.id_list = []
        self.client = self.init_client() 

    def init_client(self): 
        return tweepy.Client(bearer_token=self.bearer_token) 

    def get_ids(self): 
        with open(self.users, 'r') as f: 
            text_file = f.read().split("\n")
            for line in text_file: 
                self.userdic[line] = None 

        for user in self.userdic: 
            userinfo = list(self.client.get_user(username=user))
            self.userdic[user] = userinfo[0].id

        return self.userdic  

    def show_tweets(self): 
        id_dic = self.get_ids() 
        for i in id_dic: 
            tweet_list = list(self.client.get_users_tweets(id_dic[i]))[0]
            for j in tweet_list: 
                print(f"{i}: {j}")
            print("----------")


        


c1 = Compile("users.txt", config.BEARER_TOKEN)
print(c1.show_tweets())






