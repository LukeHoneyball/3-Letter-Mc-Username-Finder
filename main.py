import requests
import time
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                name = a+b+c
                go = False
                amt = 10
                while not go:
                    try:
                        f = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}', timeout=1)
                        resp = f.json()
                        try:
                            print(resp['id'])
                            go = True
                        except KeyError:
                            try:
                             namer = resp['name']
                             print(f"YOU CAN USE {namer}")
                             f = open("CHECK ME.txt", 'a')
                             f.write(namer + '\n')
                             f.close()
                            except KeyError:
                                print("being rate limited")
                                time.sleep(amt)
                    except requests.exceptions.ReadTimeout:
                        print("being rate limited")
                        time.sleep(amt)
                    except requests.exceptions.ConnectTimeout:
                        print("being rate limited")
                        time.sleep(amt)
                    except requests.exceptions.JSONDecodeError:
                        print("being rate limited")
                        time.sleep(amt)
                    amt += 10
                    time.sleep(1)