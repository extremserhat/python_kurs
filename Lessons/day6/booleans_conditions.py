if True:
    print('print this is...')

language = 'Python'

if language == 'Python':
    print('Conditional was True')
else:
    print('no match')

if language == 'cpp':
    print('Conditional was True')
elif language == 'Java':
    print('Languge is Java')
elif language == 'csharp':
    print('Languge is csharp')
else:
    print('no match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in: # both of this had tob true
    print('Admin Page')
else:
    print('Bad Creds')

logged_in_2 = False

if user == 'Admin' or logged_in_2:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in_2:
    print('Please log in')
else:
    print('Welcome')
