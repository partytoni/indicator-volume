#!/usr/bin/python

import os
import signal
import json

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'indicator-volume'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('volume.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_110 = gtk.MenuItem('110%')
    item_110.connect('activate', volume_110)
    menu.append(item_110)

    item_120 = gtk.MenuItem('120%')
    item_120.connect('activate', volume_120)
    menu.append(item_120)

    item_130 = gtk.MenuItem('130%')
    item_130.connect('activate', volume_130)
    menu.append(item_130)

    item_140 = gtk.MenuItem('140%')
    item_140.connect('activate', volume_140)
    menu.append(item_140)

    item_150 = gtk.MenuItem('150%')
    item_150.connect('activate', volume_150)
    menu.append(item_150)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def volume_110(_):
    os.system("pactl set-sink-volume 0 110%")

def volume_120(_):
    os.system("pactl set-sink-volume 0 120%")

def volume_130(_):
    os.system("pactl set-sink-volume 0 130%")

def volume_140(_):
    os.system("pactl set-sink-volume 0 140%")

def volume_150(_):
    os.system("pactl set-sink-volume 0 150%")

def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
