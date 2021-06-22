#!/usr/bin/env python3

import click
import os
from colorama import init, Fore, Style
from pytube import YouTube
from pytube import YouTube
from pytube.cli import on_progress


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command("download", short_help="Download YouTube videos", context_settings=CONTEXT_SETTINGS)
@click.option("--video", "-v", help="YouTube video Url", metavar="<String>")
@click.option("--file", "-f", default="video", help="Download directory", metavar="<String>")
def download(video, file):
    """
    Download YouTube videos to FAST to FURIUS
    """
    yt = YouTube(video, on_progress_callback=on_progress)
    title = yt.title
    print(title)
    stream = yt.streams.first()
    stream.download(file)


@main.command("ls", short_help="Show video list")
def ls():
    init(autoreset=True)
    print(Style.BRIGHT+"video:")
    for video in os.listdir("video"):
        print("  "+Style.NORMAL+Fore.MAGENTA+video+Style.RESET_ALL)


if __name__ == "__main__":
    main()
