# Download-Playlist
This python program uses the tkinter library along with the spotipy and pytibe API's to download all the songs of a given spotify playlist as MP3 files. 

## Authorizing Credentials

### Spotify Credentials
In order to use this program, you will need to obtain the client_ID and client_secret credentials for spotify. 

1. Create a Spotify Developer Account:
If you don't already have one, go to the Spotify Developer Dashboard and sign in or create a Spotify developer account.

2. Create a New App:
Once you're logged in, click the "Create an App" button.
Fill in the required information about your application, including its name, description, and other details.
Setup your Redirect URI: use something like 'http://localhost:8080/callback' as this is a desktop apllication running on a local server.
Agree to the Spotify Developer Terms of Service and Privacy Policy.

3. Register Your Application:
After you've created the app, click the settings button in the top right corner. Now you can see your client_ID and client_secret credentials. Paste these
credentials in the code where it asks for client_ID and and client_secret.

### YouTube Credentials
1. Create a Google Cloud Project:
Visit the [Google Cloud Console](https://console.cloud.google.com/)

2. Create A New Project:
Click the project dropdown in the top-left corner and select "Select a project"
Click the "New Project" button at the top right
Give your project a name and an organization and create the project

3. Enable the YouTube Data API:
In the Google Cloud Console, click on the hamburger menu (≡) and navigate to "APIs & Services" > "Library"
Search for "YouTube Data API" and click the "Enable" button

4. Create Credentials:
Click on the hamburger menu (≡) and navigate to "APIs & Services" > "Credentials"
Click on the "Create Credentials" button at the top and select API key
Pase this API key where it asks for the credentials in the code

## Using the Program
First, you will need to retrieve the playlist ID of the spotify playlist you want to download. This can be done by right clicking on the desired playlist >
"Share" > "Copy link to playlist". 

![Copy playlist ID](https://github.com/ajaytalanki/Download-Playlist/blob/main/images/copy%20link.png?raw=true)

Now, open the MP3IFY program.
![MP3IFY](https://github.com/ajaytalanki/Download-Playlist/blob/main/images/app.png?raw=true)

Copy and pase the playlist ID into the entry box, and select the folder you would like to download the MP3 files to.
![select](https://github.com/ajaytalanki/Download-Playlist/blob/main/images/select%20folders.png?raw=true)

Wait for the program to complete
![completion](https://github.com/ajaytalanki/Download-Playlist/blob/main/images/completion.png?raw=true)

Navigate to the destination folder and enjoy the MP3 files!
![files](https://github.com/ajaytalanki/Download-Playlist/blob/main/images/files.png?raw=true)








