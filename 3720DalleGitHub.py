import openai
import urllib
import io 
from PIL import Image, ImageDraw
import webbrowser 

# API Key
openai.api_key = 'KEY_HERE'

#Download GitHub Data
username = 'USERNAME_HERE'
avatar = Image.open(urllib.request.urlopen('https://avatars.githubusercontent.com/' + username))

width, height = avatar.size

# Create a solid color image of the same size as avatar
mask = Image.new('RGBA', (width, height), (0,0,0,255))

#Change the top third of the image to transparent
ImageDraw.Draw(mask).rectangle([0,0, (width, height // 3)], fill=(0,0,0,0))

# save to byes
avatarBytes = io.BytesIO()
avatar.save(avatarBytes, format = 'PNG')

maskBytes = io.BytesIO()
mask.save(maskBytes, format = 'PNG')

# Generate an image!
result = openai.Image.create_edit(
	image=avatarBytes.getvalue(),
	mask=maskBytes.getvalue(),
	prompt="A person with a party hat",
	n=1, 
	size= "1024x1024"
)

webbrowser.open(result['data'][0]['url'])

