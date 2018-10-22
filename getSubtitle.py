import os
import sys

from getLink import link

path = link("https://www.youtube.com/results?search_query=" +
            "+".join(sys.argv[1].split(" ")))

# print(path)
cwd = os.getcwd()
os.system(
    "youtube-dl --all-subs --write-sub --sub-lang \"en\" --skip-download -o \"{}\" {}".format(cwd, path))
# print("done")
