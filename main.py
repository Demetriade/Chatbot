import api


if __name__ == '__main__':
    data = api.open_file('intents.json')
    run = True
    
    print('----------------------------------------------------')
    while(run):
        #print(data)
        answer = input('Ask anything : ')
        print(f'Processing... waiting to understand : {answer}')

        if answer in ['exit', 'stop']:
            run = False
            print('Thanks for the chat! Have a nice day!\n')