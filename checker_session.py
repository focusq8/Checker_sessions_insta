import requests

open_file = input("Enter Your File Name: ")

with open(open_file, "r") as file:

    for line in file:
        sessions = line.strip()

        url='https://www.instagram.com/instagram/'

        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "cookie": f"sessionid={sessions}"
            }

        req = requests.get(url=url,headers=headers)

        if "no-js logged-in" in req.text:

            with open(f'working.txt', 'a') as file:
                file.write(f'\n{sessions}')
                file.close()
                print("working")

        elif 'no-js not-logged-in' in req.text:
            print("Not working")

        else:
            print(req.text)
