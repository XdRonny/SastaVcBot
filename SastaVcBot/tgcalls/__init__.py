## Copyright (©) Team GodseXD SastaVcBot 

from os import listdir, mkdir
from pyrogram import Client
from SastaVcBot import config
from SastaVcBot.tgcalls.queues import clear, get, is_empty, put, task_done
from SastaVcBot.tgcalls import queues
from SastaVcBot.tgcalls.youtube import download
from SastaVcBot.tgcalls.calls import run, pytgcalls
from SastaVcBot.tgcalls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from SastaVcBot.tgcalls.convert import convert
