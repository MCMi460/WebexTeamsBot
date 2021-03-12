from setup import token
from webexteamssdk import WebexTeamsAPI
import random
api = WebexTeamsAPI(access_token=token)
global room
room = None
while True:
    ct = input(">>> ")
    if ct.startswith("/"):
        ct.replace("/","")
    if "exit" in ct or "stop" in ct:
        break
    elif ct.startswith("help"):
        print("Command list:\n"
        "make - Makes a room and adds its room.ID to the clipboard\n"
        "join - Joins an email of your choice to the room.ID on clipboard\n"
        "say - Sends a message in the room.ID on clipboard\n"
        "choose - Shows a list of rooms the bot is currently in (DMs are displayed as \"Empty Title\")\n"
        "delete - If given operator permissions, the bot can delete the room on clipboard\n"
        "exit - Exits and terminates the script")
    elif ct.startswith("make"):
        try:
            if ct == "make":
                rng = random.randint(10000,99999)
                room = api.rooms.create(f'newroom{rng}')
                print(f"Successfully created room named \"newroom{rng}\"")
            elif ct.startswith("make "):
                ct = ct.replace("make ","")
                room = api.rooms.create(f'{ct}')
                print(f"Successfully created room named \"{ct}\"")
            else:
                print("Unknown command")
        except:
            print("Failed to create room")
    elif ct.startswith("join"):
        if ct.startswith("join "):
            email = ct.replace("join ","")
            try:
                api.memberships.create(room.id, personEmail=email)
            except:
                print("An error occurred when attempting this order.")
        elif ct == "join":
            email = input("Enter email > ")
            if "exit" in email or "stop" in email:
                break
            try:
                api.memberships.create(room.id, personEmail=email)
            except:
                print("An error occurred when attempting this order.")
        else:
            print("Unknown command")
    elif ct.startswith("say"):
        try:
            if ct == "say":
                ct = input("Please type a message > ")
                if "exit" in ct or "stop" in ct:
                    break
                api.messages.create(room.id, text=f"{ct}")
            elif ct.startswith("say "):
                ct = ct.replace("say ","")
                api.messages.create(room.id, text=f"{ct}")
            else:
                print("Unknown command")
        except:
            print("Failed to send")
    elif ct.startswith("choose"):
        try:
            worked = False
            allrooms = api.rooms.list()
            if ct == "choose":
                for every in allrooms:
                    print(every.title)
                chat = input("Please choose a chat > ")
                if "exit" in chat or "stop" in chat:
                    break
                for every in allrooms:
                    if every.title == chat:
                        room = every
                        worked = True
                if not worked:
                    print("Sorry, unknown room")
            elif ct.startswith("choose "):
                chat = ct.replace("choose ","")
                for every in allrooms:
                    if every.title == chat:
                        room = every
                        worked = True
                if not worked:
                    print("Sorry, unknown room")
            else:
                print("Unknown command")
        except:
            print("Failed to perform the task")
    elif ct.startswith("delete"):
        try:
            api.rooms.delete(room.id)
        except:
            print("Failed to delete room")
    else:
        print("Unknown command")
    continue
print("Ended session")
