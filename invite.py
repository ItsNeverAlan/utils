"""
invite
~~~~~~~~~~~~~~~~~~~~~

An extension module to help finding and replacing discord invite links
"""

import re
from fire import exceptions

dgg = r'(http|https)?(:)?(\/\/)?discord.gg\/([a-zA-Z0-9\-]+)'
dio = r'(http|https)?(:)?(\/\/)?discord.io\/([a-zA-Z0-9\-]+)'
dme = r'(http|https)?(:)?(\/\/)?discord.me\/([a-zA-Z0-9\-]+)'
dappcom = r'(http|https)?(:)?(\/\/)?discordapp.com\/invite\/([a-zA-Z0-9\-]+)'
invgg = r'(http|https)?(:)?(\/\/)?invite.gg\/([a-zA-Z0-9\-]+)'
vanity = r'(http|https)?(:)?(\/\/)?(?:oh-my-god|inv|floating-through|get-out-of-my-parking|i-live-in|i-need-personal)\.(?:wtf|space)\/([a-zA-Z0-9\-]+)'
invreplace = '[redacted invite]'

def findinvite(text: str):
	searches = [re.search(regex, text) for regex in [dgg, dio, dme, dappcom, invgg, vanity]]
	found = [s for s in searches if s]
	if len(found) >=1 and found[0]:
		return found[0].group(4)
	else:
		return False

def replaceinvite(text: str):
	message = [re.sub(regex, invreplace, text, 0, re.MULTILINE) for regex in [dgg, dio, dme, dappcom, invgg, vanity]]
	message = [m for m in message if m]
	if message[0]:
		return message[0]
	else:
		return False
