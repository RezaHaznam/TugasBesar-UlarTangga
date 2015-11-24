# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Johanes Kalas, Carissa Ulibasa, Devi Apriliani S, Jovanka Helen, Reza Haznam"
             
class Player:
	warna = ''
	mataDadu = 0
	posisi = 0
	def __init__(self, warna):
		self.warna = warna
	def getWarna(self):
		return self.warna
	def setPosition(self,x):
		self.posisi = x
	def getPosition(self):
		return self.posisi

import random

class Dice:
	mataDadu = 0
	def __init__(self):
		self.mataDadu = 0
	def getMataDadu(self):
                self.mataDadu = random.randint(1,6)
                return self.mataDadu
            
class Tile:
	player = ''
	ladderAwal = ''
	snakeAwal = ''
	def getPlayer(self):
		return self.player
	def setPlayer(self, player):
		self.player = player
	def getLadderAwal(self):
		return self.ladderAwal
	def setLadderAwal(self, ladderAwal):
		self.ladderAwal = ladderAwal
	def getSnakeAwal(self):
		return self.snakeAwal
	def setSnakeAwal(self, snakeAwal):
		self.snakeAwal = snakeAwal

class Board:
	tile = [""]
	posisiPlayer = 0
	player = ""
	mataDadu = 0
	def __init__(self):
            self.tile = range(1,101)
            self.posisiPlayer = 0
	def setPlayer(self,player):
            self.player = player
	def setPosition(self,x):
            self.posisiPlayer = self.player.getPosition() + x
            if(self.posisiPlayer > 100):
                m = self.posisiPlayer - 100
                self.posisiPlayer = 100 - m
            self.player.setPosition(self.posisiPlayer)
	def setMataDadu(self,dice):
		self.mataDadu = dice.getMataDadu()
	def getMataDadu(self):
		return self.mataDadu
	def getPlayer():
		return self.player
           
class Ladder():
	#board = Board()
    player = ''
    def __init__(self, player):
        self.player = player
    def setPosition(self, rules):
        getPosisi = self.player.getPosition()
        if rules == 1 :
            if getPosisi == 7:
                self.player.setPosition(36)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 40:
                self.player.setPosition(59)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 45:
                self.player.setPosition(78)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 53:
                self.player.setPosition(71)
                print("Tangga naik ke ",self.player.getPosition())
        elif rules == 2:
            if getPosisi == 4:
                self.player.setPosition(21)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 8:
                self.player.setPosition(30)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 28:
                self.player.setPosition(84)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 58:
                self.player.setPosition(77)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 78:
                self.player.setPosition(86)
                print("Tangga naik ke ",self.player.getPosition())
        elif rules == 3:
            if getPosisi == 17:
                self.player.setPosition(46)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 5:
                self.player.setPosition(38)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 9:
                self.player.setPosition(15)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 31:
                self.player.setPosition(82)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 49:
                self.player.setPosition(97)
                print("Tangga naik ke ",self.player.getPosition())
        elif rules == 4:
            if getPosisi == 5:
                self.player.setPosition(15)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 12:
                self.player.setPosition(31)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 33:
                self.player.setPosition(69)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 44:
                self.player.setPosition(65)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 63:
                self.player.setPosition(87)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 89:
                self.player.setPosition(94)
                print("Tangga naik ke ",self.player.getPosition())
        elif rules == 5:
            if getPosisi == 6:
                self.player.setPosition(12)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 23:
                self.player.setPosition(37)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 31:
                self.player.setPosition(49)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 34:
                self.player.setPosition(76)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 62:
                self.player.setPosition(83)
                print("Tangga naik ke ",self.player.getPosition())
            elif getPosisi == 88:
                self.player.setPosition(92)
                print("Tangga naik ke ",self.player.getPosition())
    def printRules(self,rules):
        if rules == 1:
            print("Tangga ada pada diposisi :")
            print("7 naik ke 36")
            print("40 naik ke 59")
            print("45 naik ke 78")
            print("53 naik ke 71")
        elif rules == 2:
            print("Tangga ada pada diposisi :")
            print("4 naik ke 21")
            print("8 naik ke 30")
            print("28 naik ke 84")
            print("58 naik ke 77")
            print("78 naik ke 86")
        elif rules == 3:
            print("Tangga ada pada diposisi :")
            print("17 naik ke 46")
            print("5 naik ke 38")
            print("9 naik ke 15")
            print("31 naik ke 82")
            print("49 naik ke 97")
        elif rules == 4:
            print("Tangga ada pada diposisi :")
            print("5 naik ke 15")
            print("12 naik ke 31")
            print("33 naik ke 69")
            print("44 naik ke 65")
            print("63 naik ke 87")
            print("89 naik ke 94")
        elif rules == 5:
            print("Tangga ada pada diposisi :")
            print("6 naik ke 12")
            print("23 naik ke 37")
            print("31 naik ke 49")
            print("34 naik ke 76")
            print("62 naik ke 83")
            print("88 naik ke 92")
        
class Snake():
	#board = Board()
    player = ''
    def __init__(self,player):
        self.player = player
        #self.board.setPlayer(player)
    def setPosition(self, rules):
        getPosition = self.player.getPosition()
        if rules == 1:
            if getPosition == 97:
                self.player.setPosition(66)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 89:
                self.player.setPosition(5)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 64:
                self.player.setPosition(23)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 49:
                self.player.setPosition(13)
                print("Tangga turun ke ", self.player.getPosition())
        elif rules == 2:
            if getPosition == 97:
                self.player.setPosition(79)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 89:
                self.player.setPosition(5)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 64:
                self.player.setPosition(23)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 49:
                self.player.setPosition(13)
                print("Tangga turun ke ", self.player.getPosition())
        elif rules == 3:
            if getPosition == 96:
                self.player.setPosition(88)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 86:
                self.player.setPosition(63)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 54:
                self.player.setPosition(14)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 61:
                self.player.setPosition(29)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 26:
                self.player.setPosition(3)
                print("Tangga turun ke ", self.player.getPosition())
        elif rules == 4:
            if getPosition == 91:
                self.player.setPosition(72)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 87:
                self.player.setPosition(68)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 63:
                self.player.setPosition(42)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 50:
                self.player.setPosition(32)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 53:
                self.player.setPosition(35)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 19:
                self.player.setPosition(4)
                print("Tangga turun ke ", self.player.getPosition())
        elif rules == 5:
            if getPosition == 99:
                self.player.setPosition(52)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 93:
                self.player.setPosition(72)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 63:
                self.player.setPosition(20)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 25:
                self.player.setPosition(17)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 50:
                self.player.setPosition(28)
                print("Tangga turun ke ", self.player.getPosition())
            elif getPosition == 45:
                self.player.setPosition(7)
                print("Tangga turun ke ", self.player.getPosition())
    def printRules(self,rules):
        if rules == 1:
            print("Ular ada pada diposisi :")
            print("97 turun ke 66")
            print("89 turun ke 5")
            print("64 turun ke 23")
            print("49 turun ke 13")
        elif rules == 2:
            print("Ular ada pada diposisi :")
            print("97 turun ke 79")
            print("95 turun ke 51")
            print("88 turun ke 16")
            print("52 turun ke 29")
            print("57 turun ke 40")
        elif rules == 3:
            print("Ular ada pada diposisi :")
            print("96 turun ke 88")
            print("86 turun ke 64")
            print("54 turun ke 14")
            print("61 turun ke 29")
            print("26 turun ke 3")
        elif rules == 4:
            print("Ular ada pada diposisi :")
            print("91 turun ke 72")
            print("87 turun ke 68")
            print("63 turun ke 42")
            print("50 turun ke 32")
            print("53 turun ke 35")
            print("19 turun ke 4")
        elif rules == 5:
            print("Ular ada pada diposisi :")
            print("99 turun ke 52")
            print("93 turun ke 72")
            print("63 turun ke 20")
            print("25 turun ke 17")
            print("50 turun ke 28")
            print("45 turun ke 7")
