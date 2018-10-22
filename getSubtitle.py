from __future__ import unicode_literals

import os
import argparse
import sys
import time

import colorama
import youtube_dl
from colorama import Fore, Style

import getLink

parser = argparse.ArgumentParser()
parser.add_argument('QUERY', nargs='+', help='one search query that can span either a single or multiple arguments')
parser.add_argument('-l', '--lucky', help='select first CC\'d track', action='store_true')
parser.add_argument('-c', '--convert', help='convert vtt to srt', action='store_true')
parser.add_argument('-k', '--keep', help='keep original vtt after convert to srt (depends on -c/--convert)', action='store_true')
parser.add_argument('-f', '--force-convert', help='overwrite existing vtt if any (implies -c/--convert)', action='store_true')

ydl_opts = {
    'subtitleslangs': ['en'],
    'writesubtitles': True,
    'skip_download': True,

    'ignoreerrors': True
}

def convert_vtt(filename, force):
    (fn, fe) = os.path.splitext(filename)
    nargs = ['ffmpeg']
    if force:
        nargs.append('-y')
    nargs.append('-i')
    nargs.append(filename)
    nargs.append('{}.srt'.format(fn))

    sys.stdout.flush()
    ret = os.spawnvp(os.P_WAIT, nargs[0], nargs)

    if ret != 0:
        print('convert fail, exit code: {:d}'.format(ret))
        exit(ret)

def download(args, convert=False, keep=False, force=False):
    (title, channel, href, _) = args

    dim = Style.DIM
    reset = Style.RESET_ALL

    print('+ {}{}{} :: {}'.format(dim, channel, reset, title))

    url = 'https://www.youtube.com' + href
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ret = ydl.extract_info(url)

        if ret != None:
            if convert == True:
                filename = ydl.prepare_filename(ret)
                (fn, fe) = os.path.splitext(filename)
                ext = '.en.vtt'
                fn = fn + ext
                fn = os.path.join(os.getcwd(), fn)
                if os.path.exists(fn) and os.path.isfile(fn):
                    convert_vtt(fn, force)
                if not keep:
                    os.unlink(fn)

def real_main(query, lucky, convert, keep, force):
    base = 'https://www.youtube.com/results?search_query='
    qstr = '+'.join(query)

    colorama.init()

    videos = []
    try:
        videos = getLink.links(base+qstr)
    except:
        print(Fore.RED + 'error querying youtube' + Style.RESET_ALL)
        exit(1)
    cc = list(filter(lambda x : x[3], videos))

    if len(cc) == 0:
        print(Fore.RED + 'no videos found with CC' + Style.RESET_ALL)
        exit(1)

    if (lucky):
        return download(cc[0], convert, keep, force)

    fmt = '{:d}'
    if len(cc) > 10:
        fmt = '{:02d}'
    for (i,e) in enumerate(cc):
        (title, channel, href, _) = e

        dim = Style.DIM
        reset = Style.RESET_ALL

        print((fmt + ' :: {}{}{} :: {}').format(i, dim, channel, reset, title))

    uinp = -1
    while uinp == -1:
        try:
            print('\nenter choice: ', end='')
            uinp = int(input())
        except:
            # screw you.
            exit(1)

    if uinp >= len(cc):
        # screw you too
        exit(1)

    return download(cc[uinp], convert, keep, force)

def main(args):
    args = vars(args)

    flat = []
    query = args['QUERY']
    for sw in query:
        for w in sw.split(' '):
            if w != '':
                flat.append(w)

    real_main(flat, args['lucky'], (args['convert'] or args['force_convert']), args['keep'], args['force_convert'])

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
