import api


data = api.open_file('intents.json')
run = True
    
print('----------------------------------------------------')
while(run):
    answer = input('Ask anything : ')
    tup = api.__find_tag(answer.lower(), data['intents'])
    print(api.__answer(tup[0], data['intents']))

    if answer in ['exit', 'stop', 's']:
        run = False
        print('Thanks for the chat! Have a nice day!\n')