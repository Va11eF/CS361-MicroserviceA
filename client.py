import zmq
import json


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send the request to create user
    message = {"command": 'createUser', "data": {"user": "joey"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request to create user
    message = {"command": 'createUser', "data": {"user": "garnt"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the friend request
    message = {"command": 'sendFriendRequest', "data": {"sender": "joey", "receiver": "garnt"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request to view requests
    message = {"command": 'viewFriendRequests', "data": {"user": "garnt"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request to accept request
    message = {"command": 'acceptFriendRequest', "data": {"receiver": "garnt", "sender": "joey"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request to accept request
    message = {"command": 'viewFriends', "data": {"user": "garnt"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request
    message = {"command": 'createAchievement', "data": {"user": "joey", "title": "Episode One", "description": "First podcast episode"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request
    message = {"command": 'shareAchievement', "data": {"user": "joey", "id": 1}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")

    # Send the request
    message = {"command": 'viewSharedAchievements', "data": {"user": "garnt"}}
    socket.send_json(message)
    print(f"Sent request: {message}")
    
    # Receive the response
    response = socket.recv_json()
    print(f"Recieved data: {response}\n")



if __name__ == "__main__":
    main()
