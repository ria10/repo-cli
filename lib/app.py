from .repos import Repo
import requests

def fetch_repos(user):
    url = f'https://api.github.com/users/{user}/repos'
    res = requests.get(url)
    for data in res.json():
        new_repo = Repo(data["name"])
    for number, repo in enumerate(Repo.all):
        print(number + 1, repo.name)

def get_username():
    user = input("\n Enter your GitHub username followed by enter\n")
    print(user)
    return user

class CLI():
    def __init__(self):
        self._user_input = ""

    def start(self):
        try:
            self._user_input = get_username()
            if self._user_input == 'exit':
                return self.goodbye()
            fetch_repos(self._user_input)
            self.show()
        except ValueError:
            print(f"\n Sorry {self._user_input} is not a valid GitHub user")
    
    def show(self):
        self._user_input = input("\n Enter a repository that you want to view, otherwise type exit to leave\n")
        repo = Repo.find_by_input(self._user_input)
        print(f"\n {repo.name}")

    @staticmethod
    def goodbye():
        print(f"\n Goodbye!\n")


if __name__ == '__main__':
    app = CLI()
