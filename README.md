# twitterComp 
A CLI which compiles user specified twitter timelines    

## Setup 
1) Add different twitter handles you want to show in the userlist.txt file seperated by each line 
```txt 
examplehandle
otherhandle 
anothercoolhandlename
```

2) Initialize a Compile instance and use your twitter bearer token
```python
compileExample = Compile("userlist.txt", bearer_token)
```

3) Use the different Compile methods 
```python
compileExample.show_tweets()
```

