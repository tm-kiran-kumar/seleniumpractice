import requests

#url = "https://automationexercise.com/api/productsList"

# response = requests.get(url)

# GET
# status_code = response.status_code
# print(f'Status code: {status_code}')
#
# data = response.json()
#
# response_code = data['responseCode']
# products = data['products']
#
# for product in products:
#     print(f"Product Name: {product['name']}.....Price: {product['price']}", end='\n')

# pay_load = {
#     'email' : 'test1234@test123.com'
# }
# response = requests.get('https://automationexercise.com/api/getUserDetailByEmail', json=pay_load )
# print(response.json())

# POST
# Ex: 1
# data = {
#     'first' : 'test1',
#     'second' : 'test2',
#     'third' : 20
# }
# response = requests.post(url = 'https://automationexercise.com/api/productsList', json=data)
# print(f'Status Code: {response.status_code}')
# json_data = response.json()
# print(json_data)
# print('Response Code: ', json_data['responseCode'])

# Ex: 2
# pay_load = {
#     'search_product' : 'jean'
# }
# response = requests.post(url='https://automationexercise.com/api/searchProduct', data=pay_load)
# data = response.json()
# print(data)

# Ex: 3
# verify_details = {
#     'email' : 'test1234@test123.com',
#     'password' : 'test1234'
# }
#
# response = requests.post(url = 'https://automationexercise.com/api/verifyLogin', data = verify_details)
# valid_check = response.json()
# print(f'User with {verify_details['email']} already exists: {valid_check}')


# Headers

# custom_headers = {
#     "User-Agent": "MyTestAutomationScript/1.0",
#     "Accept": "application/json"
# }
#
# response = requests.get('https://automationexercise.com', headers=custom_headers)
# print(response.headers)

# Access a specific header
# print(response.headers.get("Content-Type"))
#print(response.headers['Content-Type'])

# Authorization
# url = "https://example.com/api/protected-resource"
# token = "eyJhbGciOiJIUzI1Ni..." # Your actual token
#
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Accept": "application/json"
# }
#
# response = requests.get(url, headers=headers)
# print(response.headers)


# response = requests.get(url='https://jsonplaceholder.typicode.com/users')
# data = response.json()
# print(data)
#
# for user in data:
#     print(user['email'])