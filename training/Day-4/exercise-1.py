import requests
import sys

def get_github_data(username):
    url = "https://api.github.com/users/" + username
    try:
        r = requests.get(url,timeout=5)
        data = r.json()
        print("Name : " + data['name'])
        print("City : " + data["location"])
        print("Company : " + data["company"])
        print("Bio : " + data["bio"])
        print(f'Followers :  {data["followers"]}')
        print(f'Following :  {data["following"]}')
        print(f'Public Repositories Count : {data["public_repos"]}')

        repos_data  = requests.get(data["repos_url"]).json()
        sorted_repos = sorted(repos_data, key=lambda x:x['stargazers_count'], reverse=True)

        for repo in sorted_repos[0:5]:
            print(f'Name: {repo["name"]} Stars : {repo["stargazers_count"]} Languages : {repo["language"]}')

    except Exception as e:
            print(f"Error : {e}")


command = sys.argv[1]
get_github_data(command)