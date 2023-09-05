import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk 
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
import googleapiclient.discovery
import threading

# Create the main application window
app = tk.Tk()
app.title("MP3IFY")
app.iconbitmap('mp3.ico')
app.geometry("750x500")

# Create a Canvas for the background
canvas = Canvas(app, width = 750, height = 500)
canvas.pack(fill='both', expand=True)
background = ImageTk.PhotoImage(file='images/background.png')
canvas.create_image(0, 0, image=background, anchor = 'nw')

directions = '''
MP3IFY allows users to download every song in a given Spotify playlist as an mp3 file. Retrieve
your spotify Playlist ID by: Right clicking on the desired playlist > "Share" > "Copy Spotify URL".
Paste this URL into the Playlist ID entry, and select a folder for the mp3 files to be downloaded to.
'''

disclaimer = '''
DISCLAIMER: Most of the MP3 files available on this platform are protected by copyright law. 
Downloading, sharing, or distributing copyrighted music without proper authorization 
may be illegal in your jurisdiction. Make sure you have the necessary rights or permissions before
downloading any MP3 files.
'''

# Displays text
canvas.create_text(375, 75, text="MP3IFY", fill="white", font=("Roboto", 30))
canvas.create_text(375, 150, text=directions, fill="white", font=("Roboto", 10))
canvas.create_text(375, 220, text=disclaimer, fill="white", font=("Roboto", 10))
canvas.create_text(100, 300, text="Enter Playlist ID:", fill="white", font=("Roboto", 12))
canvas.create_text(110, 350, text="Destination Folder:", fill="white", font=("Roboto", 12))

# gets the destination folder from the user
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)  
    folder_entry.insert(0, folder_selected)
    global dest
    dest = folder_entry.get()

# command that runs when user clicks download
def download():

    # authenticates spotify credentials and YouTube API-key
    client_id = "Enter client_id"
    client_secret = "Enter client_secret"
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret) 
    API_KEY = "Enter Youtube API_KEY"
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # returns a list of the names and artists of each track in the playlist
    def get_playlist_tracks(playlist_id):

        # adds all the tracks of the playlist to an array
        try:
            results = sp.playlist_tracks(playlist_id)
        except spotipy.SpotifyException:
            messagebox.showerror("Playlist Error", message='Empty playlist or invalid laylist ID')
        except Exception:
            messagebox.showerror("Playlist Error", message='Empty playlist or invalid laylist ID')

        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        # extracts the name and artist of each track and stores in array
        track_info = []
        for track in tracks:
            info = {
                'name' : track['track']['name'],
                'artist' : track['track']['artists'][0]['name'],
            }
            track_info.append(info)
        return track_info

    # stores the name and artist of each song in the playlist
    playlist_id = playlist_id_entry.get()
    track_info = get_playlist_tracks(playlist_id)

    # searches the song on youtube and downloads the first result as an mp3
    def download_mp3(track, destination):

        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

        # extracts info from the track
        name = track['name']
        artist = track['artist']
        search = artist + " - " + name + " song"

        # gets the url of the most relevant youtube video
        search_response = youtube.search().list(
            q=search,
            type='video',
            part='id',
            maxResults=1  
        ).execute()
        id = search_response['items'][0]['id']['videoId']
        url = f"https://www.youtube.com/watch?v={id}"

        # download the video as an mp3
        youtube = YouTube(url)
        audio = youtube.streams.filter(only_audio=True).first()
        mp3_file = audio.download(output_path=destination,skip_existing=True)

    # Create a list to hold the threads
    threads = []
    
    # Define a function to download a single track and add it to the thread list
    def download_thread(track, destination):
        thread = threading.Thread(target=download_mp3, args=(track, destination))
        threads.append(thread)
        thread.start()
    
    # Download MP3 files concurrently
    for track in track_info:
        download_thread(track, dest)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    messagebox.showinfo("Download Complete", "The download has completed successfully!")

# Create text entry widgets for entering the playlist ID
playlist_id_entry = tk.Entry(app)
playlist_id_entry.configure(borderwidth=2, relief="raised", width=70)
canvas.create_window(400, 300, window=playlist_id_entry)  

# Create text entry widgets for selecting the folder
folder_entry = tk.Entry(app)
folder_entry.configure(borderwidth=2, relief="raised", width=70)
canvas.create_window(400, 350, window=folder_entry)  

## adds browse button for browsing folders
browse_button = tk.Button(app, text="Browse", command=browse_folder)
browse_button.configure(borderwidth=2, relief="raised")
canvas.create_window(650, 350, window=browse_button, height = 20)

# adds download button that downloads the playlist as mp3 files
download_button = tk.Button(app, text="Download", command=download)
download_button.configure(borderwidth=2, relief="raised")
canvas.create_window(375, 400, window=download_button, width = 100, height = 20)

app.mainloop()
