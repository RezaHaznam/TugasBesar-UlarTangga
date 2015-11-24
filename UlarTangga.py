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
           
