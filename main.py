from github import Github
import os

is_public = True

token = input('Enter your GitHub Access Token: ')
print('')
full_path = input('Provide the full path of the project: ')
print('')
username = input('Enter your Github username: ')
print('')
repo_name = input('Enter repo name: ')
print('')
is_public_or_private = input('Do you want the repo to be public [Y/N]: ')
print('')

login = Github(token)
user = login.get_user()

if is_public_or_private.lower() == 'y':
    is_public = True
    user.create_repo(repo_name, private=False)
elif is_public_or_private.lower() == 'n':
    is_public = False
    user.create_repo(repo_name, private=True)
else:
    print('Invalid answer')

try:
    os.chdir(path=full_path)
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "first commit"')
    os.system('git branch -M main')
    os.system(f'git remote add origin https://github.com/{username}/{repo_name}.git')
    os.system('git push -u origin main')
except:
    print('Something went wrong. We Couldn\'t Upload The Project. 😢')
    exit()

print('')
print('Done uploading project to GitHub. 🎉')




