import json
import requests

print('''
________         .__                          
\_____  \   ____ |  |__   ____   ______ ______
 /   |   \_/ ___\|  |  \_/ __ \ /  ___//  ___/
/    |    \  \___|   Y  \  ___/ \___ \ \___ \ 
\_______  /\___  >___|  /\___  >____  >____  >
        \/     \/     \/     \/     \/     \/ 
''')

infos_gets = []
info = ['avatar', 'name', 'username', 'url', 'twitch_url', 'status', 'title', 'followers', 'player_id', 'location']
def infos(user):
    api_result = requests.get(f'https://api.chess.com/pub/player/{user}')
    data = api_result.json()
    for i in range(len(info)):
        try:
            print(info[i], ": ", data[info[int(i)]])
        except(KeyError):
            infos_gets.append(info[i])
    

    if infos_gets == info:
        print("user not found")
    else:
        choice = input("save as txt ? [y/N]: ")
        if choice == 'y':
            file = input("file name: ")
            try:
                file = open(file, "x")
            except(FileExistsError):
                print("file already exist")
                exit()
                
            for i in range(len(info)):
                try:
                    print(data[info[i]])
                    file.write((info[int(i)]))
                    file.write(": ")
                    file.write(str(data[info[i]]))
                    file.write("\n")
                except(KeyError):
                    pass
                
        else:
            exit()






infos(input("username: "))