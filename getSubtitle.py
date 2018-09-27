import os
from getLink import link
import sys
path = link("https://www.youtube.com/results?search_query=" +
            "+".join(sys.argv[1].split(" ")))
print(path)

os.system("youtube-dl --all-subs --write-auto-sub --skip-download "+path)
print("done")
