#!/usr/bin/python
# Brew Python is !/usr/local/bin/python

import os
import sys
from os import system

from workflow import Workflow3


def get_gender(voice):
    men = ['alex', 'daniel', 'diego', 'fred', 'jorge', 'juan',
           'maged', 'thomas', 'xander', 'yuri']

    if voice.lower() in men:
        return 'icons/man.png'
    return 'icons/woman.png'


def get_voices():
    ret = {}
    voices = os.popen('say -v?').read()

    for voice_line in str(voices).split('\n'):
        voice = str(voice_line).split()
        try:
            ret[voice[0]] = voice[1]
        except:
            pass

    return ret


def emoji(country_code):
    offset = 127397

    if 'scotland' in country_code:
        return "\\U0001F3F4\\U000E0067\\U000E0062\\U000E0073\\U000E0063\\U000E0074\\U000E007F"

    a = ord(country_code[0]) + offset
    b = ord(country_code[1]) + offset

    flag = '\\U%08x\\U%08x' % (a, b)

    # to print do a flag.decode('unicode_escape')
    return flag


def main(wf):
    play = False

    if sys.argv[1] != '':
        play = True
        selected_voice = sys.argv[1]
        wf.store_data('voice', selected_voice)

    wf.logger.info('Play Status: ' + str(play))
    stored_voice = wf.stored_data('voice')
    if stored_voice is not None:
        selected_voice = wf.stored_data('voice')
        icon = get_gender(stored_voice)
        if play:
            system(
                'say -v %s Hello my name is %s!  This voice is currently selected.' % (selected_voice, selected_voice))
            wf.add_item('Current Selection: ' + stored_voice,
                        'Select this option to use this voice, otherwise select a different voice below.',
                        icon=icon,
                        valid=True,
                        arg="config::exit")

        else:
            # os.popen('say -v %s Hello my name is %s!  This voice is currently selected.' % (selected_voice, selected_voice))
            wf.add_item('Current Selection: ' + stored_voice, 'Select this option to hear a preview.',
                        arg=stored_voice,
                        icon=icon,
                        valid=True)

    voices = get_voices()
    for key, value in sorted(voices.items()):
        # print key,value
        try:
        	flag = emoji(value[3:]).decode('unicode_escape')
        except:
        	flag = ""

        wf.add_item(key + " " + flag + " [" + value + "]", 'Select this voice', arg=key, valid=True,
                    icon=get_gender(key))

    # device = soco.discovery.any_soco()
    # print device

    # print device.get_current_transport_info()
    # print device.get_current_track_info()
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])

    sys.exit(wf.run(main))
