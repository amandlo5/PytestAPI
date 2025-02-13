import json
import os
import random
import string

import pytest
import requests
from utils.apis import APIS  # Corrected the import statement to match the class file name

#pytest fixture
@pytest.fixture(scope="module")
def apis_client():
    return APIS()
#to get data
def test_getValidate(apis_client,load_res_data):
    response = apis_client.getRequest('users')
    print(response.json())
    print('-===============================================-----')
    assert response.status_code ==200
    data = response.json()
    # Specify the file path for the JSON file

    # Write the response data to the JSON file
    with open('./data/response.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    res = load_res_data[2]
    print(res['name'])


#to create data
def test_postValidate(apis_client,load_user_data):
    user_data = load_user_data['new_user']
    user_data['email'] = ''.join(random.choices(string.ascii_lowercase,k=6))+'@gmail.com'
    response = apis_client.postResquest('users',user_data)
    print(response.json())
    print("------****---------------------")
    assert response.status_code == 201

#to update data
def test_putValidate(apis_client):
    data = {
        "name": "Amol143",
        "username": "amol_qa143",
        "email": "amol_qa143@gmail.com"
    }
    response = apis_client.putRequest("users/10",data)
    print(response.text)
    assert response.status_code == 200

    print('=================================***********************')
    response = apis_client.getRequest('users')
    print(response.json())

#to delete data
def test_deleteValidate(apis_client):
    response = apis_client.deleteRequest("users/10")
    print(response.status_code)
    print(response.json())