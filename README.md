# Python Spotify API App
### Project Description
##### This project uses tkinter as GUI platform to search for playlist on Spotify of certain artist by name.


## Development
### Clone repo and setup 
1. Clone this repository and navigate to it in VS Code
2. If pipenv is not yet installed on local machine (laptop):
    Open up cmd terminal then run 'pip install pipenv'
3. In VS Code terminal:
        + Run 'pipenv shell' -To activate project virtualenv.
        + Run 'pipenv install' -To install dependencies from Pipfile.lock file
4. If new library/package need to be added, run 'pipenv install library-package-name', Pipfile and Pipfile.lock will get updated automatically.


### Run program
Create an account with Spotify For Developers URL: https://developer.spotify.com/documentation/web-api
Sign in to Spotify account, create an App and retrieve CLIENT_ID and CLIENT_SECRET.
Create .env file in project folder and add the following:
    CLIENT_ID = "Your client Id here"
    CLIENT_SECRET = "Your client secret here"
    TOKEN_URL="https://accounts.spotify.com/api/token"
    SPOTIFY_URL="https://api.spotify.com/v1/"

In VS Code terminal, run 'py main.py'... and play
