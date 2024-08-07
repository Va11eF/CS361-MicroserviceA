import sqlite3

def createUser(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()
    
    username = data['user']
    
    try:
        curr.execute('INSERT INTO users (username, friends) VALUES (?, ?)', (username, ''))
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"User {username} created."}
    except sqlite3.IntegrityError:
        conn.close()
        return {"status": "error", "message": "User already exists."}
    

def userExists(name):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    res = curr.execute('SELECT 1 FROM users WHERE username = ?', (name,)).fetchone()
    conn.close()

    if res is None:
        return False
    else:
        return True    


def sendFriendRequest(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    sender = data['sender']
    receiver = data['receiver']

    if userExists(sender) and userExists(receiver):
        curr.execute('INSERT OR IGNORE INTO friend_requests (sender, receiver) VALUES (?, ?)', (sender, receiver))
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Friend request sent from {sender} to {receiver}."}
    else:
        conn.close()
        return {"status": "error", "message": "At least one user does not exist."}


def acceptFriendRequest(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    sender = data['sender']
    receiver = data['receiver']

    if curr.execute('SELECT 1 FROM friend_requests WHERE sender = ? AND receiver = ?', (sender, receiver)).fetchone():
        curr.execute('DELETE FROM friend_requests WHERE sender = ? AND receiver = ?', (sender, receiver))
        curr.execute('UPDATE users SET friends = (SELECT CASE WHEN friends = "" THEN ? ELSE friends || "," || ? END) WHERE username = ?', (sender, sender, receiver))
        curr.execute('UPDATE users SET friends = (SELECT CASE WHEN friends = "" THEN ? ELSE friends || "," || ? END) WHERE username = ?', (receiver, receiver, sender))
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Friend request accepted from {sender}."}
    else:
        conn.close()
        return {"status": "error", "message": "Friend request does not exits."}


def denyFriendRequest(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    sender = data['sender']
    receiver = data['receiver']    
    if curr.execute('SELECT 1 FROM friend_requests WHERE sender = ? AND receiver = ?', (sender, receiver)).fetchone():
        curr.execute('DELETE FROM friend_requests WHERE sender = ? AND receiver = ?', (sender, receiver))
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Friend request from {sender} denied."}
    else:
        conn.close()
        return {"status": "error", "message": "Friend request does not exist."}


def viewFriendRequests(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    username = data['user']
    reqs = curr.execute('SELECT sender FROM friend_requests WHERE receiver = ?', (username,)).fetchall()
    conn.close()
    if reqs:
        return {"status": "success", "friend_requests": [row[0] for row in reqs]}
    else:
        return {"status": "error", "message": "No friend requests found."}


def viewFriends(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    username = data['user']

    if userExists(username):
        friendsList = curr.execute('SELECT friends FROM users WHERE username = ?', (username,)).fetchone()[0]
        if friendsList:
            return friendsList.split(',')
        else:
            return {"status": "error", "message": "No friends on list."}
    else:
        return {"status": "error", "message": "User does not exist."}


def createAchievement(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    username = data['user']
    title = data['title']
    description = data['description']

    if(userExists(username)):
        curr.execute('INSERT INTO achievements (username, title, description) VALUES (?, ?, ?)', (username, title, description))
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"{username} created achievement: {title}."}
    else:
        conn.close()
        return {"status": "error", "message": "User does not exist."}  


def achievementExists(id):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    res = curr.execute('SELECT 1 FROM achievements WHERE id = ?', (id,)).fetchone()
    conn.close()

    if res is None:
        return False
    else:
        return True 


def shareAchievment(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    username = data['user']
    id = data['id']

    if userExists(username) and achievementExists(id):
        friendsList = curr.execute('SELECT friends FROM users WHERE username = ?', (username,)).fetchone()[0]
        if friendsList:
            friendsSplit = friendsList.split(',')
            for friend in friendsSplit:
                curr.execute('INSERT OR IGNORE INTO shared_achievements (username, achievement_id) VALUES (?, ?)', (friend, id))
            conn.commit()
            conn.close()
            return {"status": "success", "message": f"Achievement shared with {username}'s friends."}
        else:
            return {"status": "error", "message": "No friends on list."}
    else :
        return {"status": "error", "message": "Invalid user or achievement ID."}


def viewSharedAchievements(data):
    #Connect to database
    conn = sqlite3.connect('user.db')
    #Assign cursor
    curr = conn.cursor()

    username = data['user']
    achievements = curr.execute('''
        SELECT a.id, a.username, a.title, a.description
        FROM shared_achievements sa
        JOIN achievements a ON sa.achievement_id = a.id
        WHERE sa.username = ?
    ''', (username,)).fetchall()

    conn.close()
    if achievements:
        return {"status": "success", "achievements": [dict(zip(['id', 'username', 'title', 'description'], row)) for row in achievements]}
    else:
        return {"status": "error", "message": "No shared achievements found."}




