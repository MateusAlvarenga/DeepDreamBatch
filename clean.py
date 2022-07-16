import os
import glob


def clean_files(pathPattern):
    for file in glob.glob(pathPattern):
        os.remove(file)


clean_files('./frames/*')
clean_files('./framesDream/*')
