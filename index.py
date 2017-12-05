# https://tonejs.github.io/MidiConvert/

import json as json
from pprint import pprint
from jinja2 import Template
import string
from random import *


def get_id():
	allchar = string.ascii_letters + string.digits
	r1 = "".join(choice(allchar) for x in range(16))
	return r1

def get_nepo(notes):
	blocks = []
	with open('note.xml') as fp:
		note = fp.read()
		fp.close()
		template = Template(note)

		for i, note in enumerate(notes):
			# pprint(note)
			r1 = get_id()
			r2 = get_id()
			r3 = get_id()
			tone = round(2**((note['midi'] - 69)/12)*440)
			dur = round(note['duration'] * 1000)
			ping = template.render(id_block=r1, id_freq=r2, id_dur=r3, tone=tone, dur=dur)
			# pprint(ping)
			blocks.append(ping)
			if i > 100:
				break
	return blocks


file = 'we-wish-you.json'
file = 'xmas-song.json'
file = 'jingle-bells.json'
file = 'tannenbaum.json'
file = 'jingbell.json'
print('file', file)
with open(file) as fp:
	music = json.load(fp)
	# pprint(music)
	print('tracks', len(music['tracks']))
	for i, tr in enumerate(music['tracks']):
		print('track', i, len(tr['notes']))
	# pprint(music['tracks'][0]['notes'])

	blocks = get_nepo(music['tracks'][1]['notes'])
	print('blocks', len(blocks))
	with open('NEPOprogBase.xml') as fp:
		xml = fp.read()
		fp.close()
		xml = xml.replace('<music/>', "\n".join(blocks))

		with open('test.xml', 'w') as ft:
			ft.write(xml)
			ft.close()
