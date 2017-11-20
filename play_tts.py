#!/usr/local/bin/python
import os
import sys
import soco



def get_speaker(speaker):
    """"Gets a speaker based on a name match"""
    for device in soco.discover():
        if device.player_name == speaker:
            return device
    return None


def main(wf):
    input_string = os.getenv('string')
    speaker = os.getenv('speaker')
    voice = os.getenv('voice')
    mp3_path = os.getenv('mp3_path')

    # url = 'x-file-cifs://iMac/share/tts.mp3' - THis is what the URL will likely look like.
    sonos_url = os.getenv('sonos_url')

    wf.logger.info('TTS String: ' + input_string)
    wf.logger.info('TTS Voice: ' + voice)
    wf.logger.info('TTS Speaker: ' + speaker)

    wf.logger.info('TTS mp3_path: ' + mp3_path)
    wf.logger.info('TTS sonos_path: ' + sonos_url)

    mp3_cmd = "say -v " + voice + " " + input_string + \
              " -o /tmp/tts.aiff && /usr/local/bin/lame --quiet -m m /tmp/tts.aiff /share/tts.mp3"
    wf.logger.info('Running cmd: ' + mp3_cmd)
    os.system(mp3_cmd)

    device = get_speaker(speaker)

    device.play_uri(sonos_url)

    print 'ARGV: ', sys.argv[0]
    print 'ENV: ', os.getenv


if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])
    wf.logger.info('STARTING TTS PROCESS')

    sys.exit(wf.run(main))
