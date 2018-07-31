from fortnite_python import Fortnite
from fortnite_python.domain import Platform  
from fortnite_python.domain import Mode
import sys                         
from tkinter import *              
from tkinter import messagebox     
import tkinter as tk               
import random                      
from PIL import ImageTk, Image     
import os                          
from datetime import datetime      
import webbrowser
from tkinter import font
from enum import Enum
import statistics


# The radiobutton list of platforms
acts = ['PS4', 'XBOX ONE', 'PC']

# The fortnite API
fortnite = Fortnite('Your API Key')

# Window adjustment
root = Tk()
root.geometry('700x600')
root.title('Fortnite Stats')
root.resizable(width=False, height=False)


root.iconbitmap(default='Images/Wallpapers/Icon.ico')

# The first wallpaper
img = ImageTk.PhotoImage(Image.open
        ("Images/Wallpapers/Wallpaper3.jpg"))                                          
panel = Label(root, image = img)                                        
panel.pack(side = "bottom", fill = "both", expand = "no")               

# The second walllpaper
img2 = ImageTk.PhotoImage(Image.open
        ("Images/Wallpapers/Wallpaper4.jpg"))                                  
panel2 = Label(root, image = img2)   


ment = StringVar()
men2 = IntVar()

# The radiobutton
platformrd = IntVar()
platformrd.set(0)

# Radiobuttons
Radiobutton(root,text='', variable = platformrd,
            value = 1).place(x = 280, y = 35)
Radiobutton(root,text='', variable = platformrd,
            value = 2).place(x = 280, y = 60)
Radiobutton(root,text='', variable = platformrd,
            value = 3).place(x = 280, y = 85)


def Search():
    panel.destroy()                          
    panel2.pack(side = "bottom", fill = "both", expand = "no")

    labelfont = ('times', 20, 'bold')


    #                 Wins Labels                      

    # Solo wins label
    statsSOLO = Label(root, text='')
    statsSOLO.place(y = 199, x = 51 , width=192)

    # Duo wins label
    statsDUO = Label(root, text='')
    statsDUO.place(y = 249, x = 51 , width=192)

    # Squad wins label
    statsSQUAD = Label(root, text='')
    statsSQUAD.place(y = 302, x = 51 , width=192)


    #            Played matches Labels            

    # Solo matches played
    statsM1 = Label(root, text='')
    statsM1.place(y = 199, x = 314, width=60)

    # Duo matches played
    statsM2 = Label(root, text='')
    statsM2.place(y = 249, x = 314, width=60)

    # Squad matches played
    statsM3 = Label(root, text='')
    statsM3.place(y = 302, x = 314, width=60)


    #                  KD Labels                            

    # Solo KD
    statsKD1 = Label(root, text='')
    statsKD1.place(y = 199, x = 477, width=70)

    # Duo KD
    statsKD2 = Label(root, text='')
    statsKD2.place(y = 249, x = 477, width=70)

    # Squad KD
    statsKD3 = Label(root, text='')
    statsKD3.place(y = 302, x = 477, width=70)


    #                 Kills Labels

    # Solo kills
    statsK1 = Label(root, text='')
    statsK1.place(y = 199, x = 586, width=72)

    # Duo kills
    statsK2 = Label(root, text='')
    statsK2.place(y = 249, x = 586, width=72)

    # Squad kills
    statsK3 = Label(root, text='')
    statsK3.place(y = 302, x = 586, width=72)


    # Wins Label
    stats_wins = Label(root, text='')
    stats_wins.place(y = 375, x = 51, width = 192)

    # Played Matches Label
    stats_matches = Label(root, text='')
    stats_matches.place(y = 375, x = 306, width = 76)

    # KD Label
    stats_kd = Label(root, text='')
    stats_kd.place(y = 375, x = 477, width=70)

    # Kills Label
    stats_kills = Label(root, text='')
    stats_kills.place(y = 375, x = 586, width=72)

    stats = platformrd.get()


    # PS4 Player
    if stats == (1):
        mtext = ment.get() # Nickname inputted by the user
        player = fortnite.player(mtext, Platform.PSN) #PS4 Platform
        
        # Solo wins
        stats1 = player.getStats(Mode.SOLO)
        wins_solo_psn = int((stats1.wins))
        statsSOLO.configure(text='SOLO: ' + stats1.wins)
        statsSOLO.configure(font=labelfont)

        # Duo wins
        stats2 = player.getStats(Mode.DUO)
        wins_duo_psn = int((stats2.wins))
        statsDUO.configure(text='DUO: ' + stats2.wins)
        statsDUO.configure(font=labelfont)

        # Squad wins
        stats3 = player.getStats(Mode.SQUAD)
        wins_squad_psn = int((stats3.wins))
        statsSQUAD.configure(text='SQUAD: ' + stats3.wins)
        statsSQUAD.configure(font=labelfont)


        # Calculation of all wins
        total_wins_psn = str(
            (wins_solo_psn + wins_duo_psn + wins_squad_psn)) 
        stats_wins.configure(text='TOTAL:  ' + total_wins_psn,
            bg = 'orange')
        stats_wins.configure(font=labelfont)


        # Played Matches(SOLO)
        stats10 = player.getStats(Mode.SOLO)
        matches_solo_psn = int((stats10.total))  
        statsM1.configure(text='' + stats10.total)
        statsM1.configure(font=labelfont)

        # Played Matches(DUO)
        stats11 = player.getStats(Mode.DUO)
        matches_duo_psn = int((stats11.total))   
        statsM2.configure(text='' + stats11.total)
        statsM2.configure(font=labelfont)

        # Played Matches(SQUAD)
        stats12 = player.getStats(Mode.SQUAD)
        matches_squad_psn = int((stats12.total))   
        statsM3.configure(text='' + stats12.total)
        statsM3.configure(font=labelfont)


        # Calculation of all played matches
        total_matches_psn = str(
            (matches_solo_psn + matches_duo_psn + matches_squad_psn))
        stats_matches.configure(text='' + total_matches_psn,
            bg = 'orange')
        stats_matches.configure(font=labelfont)


        # KD(SOLO)
        stats19 = player.getStats(Mode.SOLO)  
        statsKD1.configure(text='' + stats19.kd)
        statsKD1.configure(font=labelfont)

        # KD(DUO)
        stats20 = player.getStats(Mode.DUO)
        statsKD2.configure(text='' + stats20.kd)
        statsKD2.configure(font=labelfont)

        # KD(SQUAD)
        stats21 = player.getStats(Mode.SQUAD) 
        statsKD3.configure(text='' + stats21.kd)
        statsKD3.configure(font=labelfont)


        # Calculation of the KD
        total_kd_psn = (stats19.kd, stats20.kd, stats21.kd)
        kd_psn1 = (map(float, total_kd_psn))
        kd_psn2 = (float(statistics.mean(kd_psn1)))
        kd_psn3 = round(kd_psn2, 2)
        stats_kd.configure(text='' + str(kd_psn3), bg = 'orange')
        stats_kd.configure(font=labelfont)
        

        # Kills(SOLO)
        stats31 = player.getStats(Mode.SOLO)
        kills_solo_psn = int((stats31.kills))
        statsK1.configure(text='' + stats31.kills)
        statsK1.configure(font=labelfont)

        # Kills(DUO)
        stats32 = player.getStats(Mode.DUO)
        kills_duo_psn = int((stats32.kills))
        statsK2.configure(text='' + stats32.kills)
        statsK2.configure(font=labelfont)

        # Kills(SQUAD)
        stats33 = player.getStats(Mode.SQUAD)
        kills_squad_psn = int((stats33.kills))
        statsK3.configure(text='' + stats33.kills)
        statsK3.configure(font=labelfont)


        # Calculation of all the kills
        total_kills_psn = str((kills_solo_psn + kills_duo_psn +
                               kills_squad_psn))
        stats_kills.configure(text='' +
                               total_kills_psn, bg = 'orange')
        stats_kills.configure(font=labelfont)

    # PC Player
    if stats == (2):
        mtext = ment.get() # Nickname inputted by the user
        player2 = fortnite.player(mtext, Platform.PC) # PC Platform

        # Solo wins
        stats4 = player2.getStats(Mode.SOLO)
        wins_solo_pc = int((stats4.wins))
        statsSOLO.configure(text='SOLO: ' + stats4.wins)
        statsSOLO.configure(font=labelfont)

        # Duo wins
        stats5 = player2.getStats(Mode.DUO)
        wins_duo_pc = int((stats5.wins)) 
        statsDUO.configure(text='DUO: ' + stats5.wins)
        statsDUO.configure(font=labelfont)

        # Squad wins
        stats6 = player2.getStats(Mode.SQUAD)
        wins_squad_pc = int((stats6.wins)) 
        statsSQUAD.configure(text='SQUAD: ' + stats6.wins)
        statsSQUAD.configure(font=labelfont)

        # Calculation of all wins
        total_wins_pc = str(
            (wins_solo_pc + wins_duo_pc + wins_squad_pc))
        stats_wins.configure(text='TOTAL:  ' +
                             total_wins_pc, bg = 'orange')
        stats_wins.configure(font=labelfont)

        # Played matches(SOLO)
        stats13 = player2.getStats(Mode.SOLO)
        matches_solo_pc = int((stats13.total))  
        statsM1.configure(text='' + stats13.total)
        statsM1.configure(font=labelfont)

        # Played matches(DUO)
        stats14 = player2.getStats(Mode.DUO)
        matches_duo_pc = int((stats14.total))   
        statsM2.configure(text='' + stats14.total)
        statsM2.configure(font=labelfont)

        # Played matches(SQUAD)
        stats15 = player2.getStats(Mode.SQUAD)
        matches_squad_pc = int((stats15.total))   
        statsM3.configure(text='' + stats15.total)
        statsM3.configure(font=labelfont)


        # Calculation of all played matches
        total_matches_pc = str((matches_solo_pc + matches_duo_pc +
                                matches_squad_pc))
        stats_matches.configure(text='' +
                                total_matches_pc, bg = 'orange')
        stats_matches.configure(font=labelfont)


        # KD(SOLO)
        stats22 = player2.getStats(Mode.SOLO)                 
        statsKD1.configure(text='' + stats22.kd)
        statsKD1.configure(font=labelfont)

        # KD(DUO)
        stats23 = player2.getStats(Mode.DUO)                 
        statsKD2.configure(text='' + stats23.kd)
        statsKD2.configure(font=labelfont)

        # KD(SQUAD)
        stats24 = player2.getStats(Mode.SQUAD)        
        statsKD3.configure(text='' + stats24.kd)
        statsKD3.configure(font=labelfont)


        # Calculation of the KD
        total_kd_pc = (stats22.kd, stats23.kd, stats24.kd)
        kd_pc1 = (map(float, total_kd_pc))
        kd_pc2 = (float(statistics.mean(kd_pc1)))
        kd_pc3 = round(kd_pc2, 2)
        stats_kd.configure(text='' + str(kd_pc3), bg = 'orange')
        stats_kd.configure(font=labelfont)

        # Kills(SOLO)
        stats28 = player2.getStats(Mode.SOLO)
        kills_solo_pc = int((stats28.kills))
        statsK1.configure(text='' + stats28.kills)
        statsK1.configure(font=labelfont)

        # Kills(DUO)
        stats29 = player2.getStats(Mode.DUO)
        kills_duo_pc = int((stats29.kills))
        statsK2.configure(text='' + stats29.kills)
        statsK2.configure(font=labelfont)

        # Kills(SQUAD)
        stats30 = player2.getStats(Mode.SQUAD)
        kills_squad_pc = int((stats30.kills))
        statsK3.configure(text='' + stats30.kills)
        statsK3.configure(font=labelfont)


        # Calculation of all the kills
        total_kills_pc = str((kills_solo_pc +
                              kills_duo_pc + kills_squad_pc))
        stats_kills.configure(text='' +
                              total_kills_pc, bg = 'orange')
        stats_kills.configure(font=labelfont)

    # XBOX Player
    if stats == (3):
        mtext = ment.get() # Nickname inputted by the user
        player3 = fortnite.player(mtext, Platform.XBOX) # XBOX Platform

        # Solo wins
        stats7 = player3.getStats(Mode.SOLO)
        wins_solo_xb = int((stats7.wins)) 
        statsSOLO.configure(text='SOLO: ' + stats7.wins)
        statsSOLO.configure(font=labelfont)

        # Duo wins
        stats8 = player3.getStats(Mode.DUO)
        wins_duo_xb = int((stats8.wins))  
        statsDUO.configure(text='DUO: ' + stats8.wins)
        statsDUO.configure(font=labelfont)

        # Squad wins
        stats9 = player3.getStats(Mode.SQUAD)
        wins_squad_xb = int((stats9.wins))  
        statsSQUAD.configure(text='SQUAD: ' + stats9.wins)
        statsSQUAD.configure(font=labelfont)


        # Calculation of all wins
        total_wins_xb = str((wins_solo_xb +
                             wins_duo_xb + wins_squad_xb))
        stats_wins.configure(text='TOTAL:  ' +
                             total_wins_xb, bg = 'orange')
        stats_wins.configure(font=labelfont)


        # Played matches(SOLO)
        stats16 = player3.getStats(Mode.SOLO)
        matches_solo_xb = int((stats16.total) )
        statsM1.configure(text='' + stats16.total)
        statsM1.configure(font=labelfont)

        # Played matches(DUO)
        stats17 = player3.getStats(Mode.DUO)
        matches_duo_xb = int((stats17.total))  
        statsM2.configure(text='' + stats17.total)
        statsM2.configure(font=labelfont)

        # Played matches(SQUAD)
        stats18 = player3.getStats(Mode.SQUAD)
        matches_squad_xb = int((stats18.total))                      
        statsM3.configure(text='' + stats18.total)
        statsM3.configure(font=labelfont)


        # Calculation of all played matches
        total_matches_xb = str((matches_solo_xb + matches_duo_xb +
                                matches_squad_xb))
        stats_matches.configure(text='' +
                                total_matches_xb, bg = 'orange')
        stats_matches.configure(font=labelfont)


        # KD(SOLO)
        stats25 = player3.getStats(Mode.SOLO)                 
        statsKD1.configure(text='' + stats25.kd)
        statsKD1.configure(font=labelfont)

        # KD(DUO)
        stats26 = player3.getStats(Mode.DUO)                 
        statsKD2.configure(text='' + stats26.kd)
        statsKD2.configure(font=labelfont)

        # KD(SQUAD)
        stats27 = player3.getStats(Mode.SQUAD)                  
        statsKD3.configure(text='' + stats27.kd)
        statsKD3.configure(font=labelfont)


        # Calculation of the KD
        total_kd_xb = (stats25.kd, stats26.kd, stats27.kd)
        kd_xb1 = (map(float, total_kd_xb))
        kd_xb2 = (float(statistics.mean(kd_xb1)))
        kd_xb3 = round(kd_xb2, 2)
        stats_kd.configure(text='' + str(kd_xb3), bg = 'orange')
        stats_kd.configure(font=labelfont)

        # Kills(SOLO)
        stats34 = player3.getStats(Mode.SOLO)
        kills_solo_xb = int((stats34.kills))
        statsK1.configure(text='' + stats34.kills)
        statsK1.configure(font=labelfont)

        # Kills(DUO)
        stats35 = player3.getStats(Mode.DUO)
        kills_duo_xb = int((stats35.kills))
        statsK2.configure(text='' + stats35.kills)
        statsK2.configure(font=labelfont)

        # Kills(SQUAD)
        stats36 = player3.getStats(Mode.SQUAD)
        kills_squad_xb = int((stats36.kills))
        statsK3.configure(text='' + stats36.kills)
        statsK3.configure(font=labelfont)


        # Calculation of all the kills
        total_kills_xb = str((kills_solo_xb +
                              kills_duo_xb + kills_squad_xb))
        stats_kills.configure(text='' +
                              total_kills_xb, bg = 'orange')
        stats_kills.configure(font=labelfont)


# Entry box
entryBox = Entry(root,textvariable=ment)
entryBox.place(x = 280, y = 5)

# Search button
Button(root, text='Search', command=Search).place(x = 410, y = 5)

root.mainloop()
