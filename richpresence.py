from pypresence import Presence
import time

client_id = ''

RPC = Presence(client_id=client_id)
RPC.connect()
print ('Client successfully connected.')

# Rich Presence settings
RPC.update(
    state="How to make",
    details="Discord Rich Presence",
    start=time.time(),
    large_image="url",
    large_text="Your Game Name",
    small_image="url",
    small_text="Your Game Mode",
    buttons= [{"label": "🎮 Steam", "url": "https://"},
              {"label": "🌎 GitHub", "url": "https://"}]
)

try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    print('Program terminated.')
