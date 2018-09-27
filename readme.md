# Grab subtitle from Youtube by Title

## Intallation Notes

- Git clone the repo and cd. _This Guide assumes you've cloned at $HOME, Change the alias location accordingly_
- Install youtube-dl `sudo apt-get install youtube-dl`
- Install required libraries `pip3 install -r requirements.txt`

## Usage

1. Add `alias getsub='python3 ~/Youtube-Sub-ByTitle/getSubtitle.py'` to ~/.bashrc.
2. Go to the location containg the Video or Audio file.
3. Append Subtitle using `getsub <Title> [<Artist>,<Additional Parameters>]`.

   3.1 Example:

   - `getsub 'Fall Eminem'`

### Report Issues if you find any _[you probably will]_.
