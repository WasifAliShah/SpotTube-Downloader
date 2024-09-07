from googleapiclient.discovery import build
from dotenv import load
import os
import base64
from requests import post,get
import json
import yt_dlp
import concurrent.futures

# create a .env file that should be of the form:
CLIENT_ID ="Your Spotify Client ID" # go to developer.spotify.com create a new project and copy it
CLIENT_SECRET ="Your Spotify Client ID" # go to developer.spotify.com create a new project and copy it
YOUTUBE_KEY="Your Youtube Key" # go to console.cloud.google.com create a new project select Youtube Data API V3 and copy it

load() # this function will automatically load our environment variables files for us
# its only going to load them if you have named them .env
client_id = os.getenv("CLIENT_ID") # which will get the value of environment variable client_ID
client_secret = os.getenv("CLIENT_SECRET")
youtube_key = os.getenv("YOUTUBE_KEY")

# getting the temporary acess token
def get_token():
    # we need to send a post request to /api/token end point including headers and query string parameters 
    # aka client_id, clien_secret and encoded in base64 thatswhat we need to send to retrieve our auth token
    auth_string = client_id + ":"+ client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")


    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    # this is where we will be sending our authorization data and where it will verif everything is correct
    # and then send back to us the token

    result = post(url, headers=headers, data=data) # data is the body of the request
    # result is goint to have some json data in a field called content
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


# creating another func for convenience that will kind of construct the header that we need whenever we are sending 
# another request
def get_auth_headers(token):
    #To use the access token you must include the following header in your API calls:
    return {"Authorization": "Bearer " + token} # authorization header for any future requests
    

# returns the user's spotify playlist 
def get_playlist(token):
    playlist_id = "0k9qCXDnFHGepIAK4rdntR"
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}?"
    headers = get_auth_headers(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

# request = youtube.channels().list()
def request_song_id(song):
    request = youtube.search().list(
            part="snippet",
            maxResults=25,
            q=song,
        )
    return request

# fuction to download and convert video form mp4 to mp3
def mp3_downloader(link):
    SAVE_PATH = "/songs"  # Update the path where you want to save the audio
    ydl_opts = {
    'format': 'bestaudio/best',  # Select the best audio quality
    'outtmpl': f'{SAVE_PATH}/%(title)s.%(ext)s',  # Name and save location
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Convert audio to mp3 format
        'preferredquality': '192',  # Set quality (192 kbps)
    }],
    'ffmpeg_location': 'C:\\ffmeg\\ffmpeg-2024-08-28-git-b730defd52-full_build\\bin',  # location of your ffmeg.exe
    # 'quiet': True,  # Suppress all yt-dlp output
    # 'no_warnings': True  # Suppress warnings
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        song_title = info_dict.get('title', 'Unknown Song')
        try:
            ydl.download([link])
            print(f'Audio downloaded successfully for song: {song_title}')
        except Exception as e:
            print(f"Failed to download: {song_title}. Error: {e}")



if __name__ == '__main__':

    songs = []

    token = get_token() # we have our temporary access token
    result = get_playlist(token)   # returns the playlist

    for item in result["tracks"]["items"]:
        songs.append(item["track"]["name"])

    youtube = build('youtube', 'v3', developerKey=youtube_key) # gives us back an service object takes api name as argument like
    # youtube to use its methods and query the api  

    song_urls = []
    for song in songs:
        request = request_song_id(song)
        response = request.execute()
        video_id = response["items"][0]["id"]["videoId"]
        link = f"https://www.youtube.com/watch?v={video_id}"
        song_urls.append(link)
    
    # download the songs using multiprocessing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(mp3_downloader,song_urls) 




