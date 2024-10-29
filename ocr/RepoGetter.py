import requests

def get_github_clone_links(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve repositories for user {username}")
        return None
    
    repos = response.json()
    clone_links = [repo['clone_url'] for repo in repos]
    
    return clone_links


username = "Example".strip()  
clone_links = get_github_clone_links(username)
for link in clone_links:
    print(link)
