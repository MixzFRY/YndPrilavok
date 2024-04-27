import requests
import configuration
import data


def post_new_user(body):
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return requests.post(url, json=body, headers=data.headers)


response = post_new_user(data.user_body)


def auth():
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    new_data = data.user_body.copy()
    del new_data['firstName']
    return requests.post(url, json=new_data, headers=data.headers)


print(response.status_code)
print(response.json())


def post_new_client_kit(kit_create, authToken):
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH

    new_headers = data.headers.copy()
    new_headers['Authorization'] = 'Bearer {authToken}'

    return requests.post(url, json=kit_create, headers=new_headers)


response = post_new_client_kit(data.kit_create, auth)

print(response.status_code)
print(response.json())
