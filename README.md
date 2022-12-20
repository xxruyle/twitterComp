# twitterComp 
A CLI which compiles user specified twitter timelines    

## Setup 
1) Add different twitter handles you want to show in the userlist.txt file seperated by each line 
```txt 
examplehandle
otherhandle 
anothercoolhandlename
```

2) initialize a Compile instance and use your twitter bearer token
```python
compileExampele = Compile("userlist.txt", bearer_token)
```

