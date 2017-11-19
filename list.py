#!/usr/bin/python
# The old one is !/usr/local/bin/python

import os,sys
from workflow import Workflow3


def get_icon(speaker):

	prefix = 'images/'
	model = speaker.get_speaker_info()['model_name']

	if model == 'Sonos CONNECT:AMP':
		return prefix + 'ZP120.png'
	if model == 'Sonos PLAY:1':
		return prefix + 'S1.png'
	if model == 'Sonos PLAY:3':
		return prefix + 'S3.png'
	if model == 'Sonos PLAY:5':
		return prefix + 'S5.png'

	print("NO ICON FOR: [" + model + ']')
	return None

def main(wf):

	try:
		if sys.argv[1] != '':
			selected_speaker = str(sys.argv[1])
			wf.store_data('speaker_name',selected_speaker)
	except:
		pass

	stored_player = wf.stored_data('speaker_name')

	for zone in soco.discover():
		#Q% print zone.player_name
		#print zone.ip_address
		radio = str(zone.is_playing_radio)
		line = str(zone.is_playing_line_in)
		vis = str(zone.is_visible)
		bridge = str(zone.is_bridge)

		state = zone.get_current_transport_info()['current_transport_state']
		info = zone.get_current_track_info()
		name = zone.player_name
		icon = get_icon(zone)
		model = zone.get_speaker_info()['model_name']
		# print(icon)



		# sub = ",".join([zone.ip_address, state,])
		# if zone.player == player:
			# wf.add_item('SELECTED: ' + zone.player_name, sub)
		# else:
		# if icon:
		selected_text = ""
		sub = 'Select this speaker to use it for TTS Playback'
		if stored_player == name:
			selected_text = " [SELECTED]"
			sub = 'This speaker is currently selected - pick a different one to change the setting'

		title = "%s [%s]%s" % (name,model,selected_text)
		#sub = '[' + model + ']'
		#sub 'Select this '
		wf.add_item(title,sub, icon=icon, arg=name, valid=True)
		
		# else:
		# 	print('NO ICON')
		# 	wf.add_item('' + zone.player_name, sub)



	#device = soco.discovery.any_soco()
	#print device
	
	#print device.get_current_transport_info()
	#print device.get_current_track_info()
	wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])
    # Call soco insde of here cause we've setup the search path already
    import soco

    wf.logger.info("HI")
    sys.exit(wf.run(main))