import zmq
import userDB


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    
    print("Server is listening...")
    while True:
        message = socket.recv_json()
        command = message.get('command')
        data = message.get('data')

        match command:
            case "createUser":

                print(f"Recieved command: {command}")
                res = userDB.createUser(data)
                print(f"Sending data: {res}\n")

            case "sendFriendRequest":
                print(f"Recieved command: {command}")
                res = userDB.sendFriendRequest(data)
                print(f"Sending data: {res}\n")

            case "acceptFriendRequest":
                print(f"Recieved command: {command}")
                res = userDB.acceptFriendRequest(data)
                print(f"Sending data: {res}\n")

            case "denyFriendRequest":
                print(f"Recieved command: {command}")
                res = userDB.denyFriendRequest(data)
                print(f"Sending data: {res}\n")

            case "viewFriendRequests":
                print(f"Recieved command: {command}")
                res = userDB.viewFriendRequests(data)
                print(f"Sending data: {res}\n")

            case "viewFriends":
                print(f"Recieved command: {command}")
                res = userDB.viewFriends(data)
                print(f"Sending data: {res}\n")

            case "createAchievement":
                print(f"Recieved command: {command}")
                res = userDB.createAchievement(data)
                print(f"Sending data: {res}\n")

            case "shareAchievement":
                print(f"Recieved command: {command}")
                res = userDB.shareAchievment(data)
                print(f"Sending data: {res}\n")

            case "viewSharedAchievements":
                print(f"Recieved command: {command}")
                res = userDB.viewSharedAchievements(data)
                print(f"Sending data: {res}\n")

            case _:
                res = {"status": "error", "message": "Unknown request type."}
                print(f"Sending data: {res}\n")

        socket.send_json(res)


if __name__ == "__main__":
    main()