import twitterComp 
import argparse 

def main(): 
    c1 = twitterComp.Compile("users.txt", twitterComp.BEARER_TOKEN)
    c1.show_tweets()

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description = "Show a user specificed twitter timeline")
    args = parser.parse_args()
    main()