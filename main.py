import tweepy 
import config 

def main(): 
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN) 
    #print(client.get_users_tweets("1093317430745726977"))
    test = list(client.get_user(username="ArrowheadLive"))
    print(test[0].id)

if __name__ == "__main__": 
    main()