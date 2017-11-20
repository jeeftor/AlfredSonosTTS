#!/usr//bin/python

import commands
import os
import sys

from workflow import Workflow3


def main(wf):
    # Figure out if LAME is installed
    lame_search_path = os.getenv('lame_search_path')
    result_tuple = commands.getstatusoutput('type ' + lame_search_path)
    wf.logger.info('Result of LAME search ', result_tuple)

    status = result_tuple[0]  # 0 if lame was found
    output = result_tuple[1]  # cmd output (we dont realy use it)

    # A valid setup will allow for TTS to occur
    valid_setup = True

    voice = wf.stored_data('voice')
    speaker = wf.stored_data('speaker_name')

    if status not in [0, '0']:
        wf.add_item('The LAME mp3 encoder is not installed',
                    "Select this option to try to install it with homebrew: 'brew install lame'",
                    arg='config::InstallLame',
                    icon='icons/icons8-nothing_found.png',
                    valid=True)
        valid_setup = False

    if voice is None:
        wf.add_item('No voice Selected', 'Select this option to pick a different voice',
                    arg='config::SelectVoice',
                    icon='icons/icons8-nothing_found.png',
                    valid=True)
        valid_setup = False

    if speaker is None:
        wf.add_item('No Speaker Selected', 'Select this option to use a different Sonos Speaker',
                    arg='config::SelectSpeaker',
                    icon='icons/icons8-nothing_found.png',
                    valid=True)
        valid_setup = False

    if valid_setup:
        item = wf.add_item('Play TTS String: ' + sys.argv[1], 'Voice: ' + voice + '  Speaker: ' + speaker, valid=True)
        item.setvar('voice', voice)
        item.setvar('speaker', speaker)
        item.setvar('string', sys.argv[1])

        wf.add_item('Change Voice', 'Select this option to pick a different voice', arg='config::SelectVoice',
                    valid=True)
        wf.add_item('Change Speaker', 'Select this option to use a different Sonos Speaker',
                    arg='config::SelectSpeaker', valid=True)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])

    sys.exit(wf.run(main))
