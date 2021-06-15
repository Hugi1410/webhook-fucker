import requests
import time
import json

def spam():
    n = 0
    webhookURL = input("\nEntez URL du webhook:\n")
    message = input("Le message a aenvoyer:\n")
    username = input("Le nomdu bot:\n")
    amount = int(input("Le nombres de messages:\n"))

    payload = {
      'content': message,
      'username': username,
    }

    for i in range(amount):
        req = requests.post(webhookURL, data=payload)
        n +=1
        print(n,"/",amount)
        time.sleep(0.2) # sleep so it doesnt timeout
      
    menu()

def delete():
    
    webhookURL = input("\nEntez URL du webhook:\n")
    requests.delete(webhookURL)
    
    print("Webhook delete")

    menu()
    
def info():
    webhookURL = input("\nEntez URL du webhook:\n")
    try:
        req = requests.get(webhookURL)
        y = json.loads(req.content)
    
        print("\nNom:",y['name'])
        print("token:",y['token'])
        print("id:",y['id'])
        print("channel id:",y['channel_id'])
        print("serveur id:",y['guild_id'])
        menu()
    except:
        print("Le wbhook n'existe pas")


        
def menu():
    print ("\n[1] - Webhook spammer")
    print ("[2] - Webhook delete")
    print ("[3] - Webhook info")
    r = input("Choisis uneoption [1-3]: ")
    
    if r == '1':
        spam()
    elif r == '2':
        delete()
    elif r == '3':
        info()
menu()
