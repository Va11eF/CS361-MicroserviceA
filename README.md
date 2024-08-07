Microservice A - Achievement Sharing and Friend Service\
Before you start anything, run createUserDB.py to initialize your database
```
    python createUserDB.py
```
In order to request data from the microservice you must first connect to the ZeroMQ socket, specifically "tcp://localhost:5555".\
Example:
```
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
```
Once connected, you cna create a message variable containing the request in the format {"command": '', "data": {"": ""}}\
Examples:
```
    message = {"command": 'createUser', "data": {"user": "garnt"}}
```
```
    message = {"command": 'sendFriendRequest', "data": {"sender": "joey", "receiver": "garnt"}}
```

List of commands with example code:\
  createUser - 
```
  message = {"command": 'createUser', "data": {"user": "garnt"}}
```
  sendFriendRequest - 
```
  message = {"command": 'sendFriendRequest', "data": {"sender": "joey", "receiver": "garnt"}}
```
  acceptFriendRequest - 
```
  message = {"command": 'acceptFriendRequest', "data": {"receiver": "garnt", "sender": "joey"}}
```
  denyFriendRequest - 
```
  message = {"command": 'denyFriendRequest', "data": {"receiver": "garnt", "sender": "joey"}}
```
  viewFriendRequests - 
```
  message = {"command": 'viewFriendRequests', "data": {"user": "garnt"}}
```
  viewFriends - 
```
  message = {"command": 'viewFriends', "data": {"user": "garnt"}}
```
  createAchievement - 
```
  message = {"command": 'createAchievement', "data": {"user": "joey", "title": "Episode One", "description": "First podcast episode"}}
```
  shareAchievement - 
```
  message = {"command": 'shareAchievement', "data": {"user": "joey", "id": 1}}
```
  viewSharedAchievements - 
```
  message = {"command": 'viewSharedAchievements', "data": {"user": "garnt"}}
```
Once message has been created you can send the request through ZeroMQ with the following line of code: socket.send_json(message)\
\
How to recieve data from the microservice:\
Once the message has sent as specified above, your program will just have to wait for a response from the microservice with the following line of code: 
```
  response = socket.recv_json()
```
The response variable will contain all the data sent from the microservice\
\
This is the UML Sequence Diagram that shows the process.
\
<img width="825" alt="image" src="https://github.com/user-attachments/assets/1005cb31-5025-432f-896f-17a6081a71a8">

