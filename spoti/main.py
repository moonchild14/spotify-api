import requests
from twitchio.ext import commands
from multiprocessing import Process

SPOTIFY_ACCESS_TOKEN = '' # Spotify token

SPOTIFY_GET_CURRENT_TRACK_URL='https://api.spotify.com/v1/me/player/currently-playing' # Link to request


twich_token = '' # Token - your twich chat-bot token
twich_channel = '' # The name of the channel on which the bot will work

def main():
    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

def get_current_track(access_token):
    response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL, headers={"Authorization": f"Bearer {access_token}"}) # Connect to spotify with access token and get array with data
    global resp_json
    resp_json = response.json() # Make variable and return it
    return resp_json



class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=twich_token, prefix='!', initial_channels=[twich_channel])
        # Token - your twich chat-bot token
        # Prefix - The prefix with which the bot will define commands
        # initial_channels - The name of the channel on which the bot will work     
    
    async def event_ready(self):
        print(f"Connected to {twich_channel}") # If the connection to twich was successful

    @commands.command()
    async def track(self, ctx: commands.Context): #Trigger command - !track
            main()
            # If the user does not have a song enabled, then we will not be able to get data from the resp_json array, so we use try.
            try:
                # We get artists and track name from json answer
                artists = resp_json['item']['artists']
                artists_name = ', '.join(
                    [artist['name'] for artist in artists])
                track_name = resp_json['item']['name']
                await ctx.send(f'{twich_channel} now listen:\n {artists_name} - {track_name}')
            except:
                await ctx.send(f"{twich_channel} not listening to anything right now =(")










if __name__ == '__main__':
    bot = Bot()
    p2 = Process(target=bot.run())
    p2.start()
    p2.join()


