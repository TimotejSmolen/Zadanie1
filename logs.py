import datetime

counter = 0
file1 = open("calls.txt", "w")

def log_invite(origin, destination):
    global counter
    file1 = open("calls.txt", "a")
    file1.write(f"CALL {counter}\nTime:{datetime.datetime.now()} {origin.split(';')[0].split('@')[0]} at {origin.split(';')[1]} is calling for {destination.split(';')[0].split('@')[0]} at {destination.split(';')[1]}\n")
    file1.close()
    counter += 1

def log_bye(origin, destination):
    file1 = open("calls.txt", "a")
    file1.write(f"Time:{datetime.datetime.now()} {origin.split('@')[0]} ended the call with {destination.split('@')[0]}\n")
    file1.close()

