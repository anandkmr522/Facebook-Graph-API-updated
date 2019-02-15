import facebook

# ask user to enter token
token = input("enter your access token: ")

# call GraphAPI with the token
graph = facebook.GraphAPI(access_token=token)

# store the user details in an object
post = graph.get_object(id='me', fields='id,name,posts,hometown,likes')

# print user details
print('USER ID:', post['id'])
print('USER NAME:', post['name'])
print('USER HOMETOWN:', post['hometown']['name'])

print("--------------------USER POSTS------------------------")
for message in post['posts']['data']:
    try:
        print(message['message'])
    except KeyError:
        pass
print('-------------------USER LIKED PAGES--------------------')
for page in post['likes']['data']:
    print(page['name'])