#!/usr/bin/python

import os, sys
from workflow import Workflow3


def main(wf):
    if sys.argv[1] != '':
        selected_speaker = str(sys.argv[1])
        wf.store_data('speaker_name', selected_speaker)


if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])
    sys.exit(wf.run(main))
