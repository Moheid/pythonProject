passwordFile = open('SecrretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typePassword = input()
if typePassword == secretPassword:
    print('Access granted')
    if typePassword == '12345':
        print('That password is one that an idiot puts on their luggage')
    else:
        print('Access denied')