import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")
nirvana_url = urlopen("https://media.giphy.com/media/Mjl0BsAgMGYTe/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target=r"conding\20_projects\animated1_qrcode.gif",
    scale=10,
    border=2
    
)
