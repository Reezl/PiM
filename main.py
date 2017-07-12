import time, threading
import pygame, sys, os, time
import mdtkinter


class Main_Screen:
	def __init__(self):
	
		self.screen = (1000,600)
		self.clock = pygame.time.Clock()
		self.list_music = []
	
	def keyboards(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
	def load_notas(self):
		if len(self.list_music) == 0:
			for mus in os.listdir('audios/'):
				self.list_music.append(mus)
			
		#return self.list_music
	def tocar_nota(self, nota):
		musics = self.list_music
		pygame.mixer.music.load('audios/'+nota+'.wav')
		pygame.mixer.music.play(0)
		#pygame.time.Clock().tick(2)
		
		time.sleep(0.35)
		
	def juncao_notas(self, nota,qt):
		
		'''
		for i in range(qt+1):
			if i%2==0:
				print(i)
				notas = 'audios/'+nota[i]+'.wav'
				pygame.mixer.Channel(i).play(pygame.mixer.Sound(notas))
		#'''
		#'''
		for i in range(qt+1):
			if i%2==0:
				notas = 'audios/'+nota[i]+'.wav'
				pygame.mixer.Channel(i).queue(pygame.mixer.Sound(notas))
				pygame.time.Clock().tick(10)
		#time.sleep(0.5)
		#'''
	
	
	def loop(self):
		self.screen = pygame.display.set_mode(self.screen)
		running = True
		notas = []
		d = []
		
		try:
			arq = open('notas.txt','r')
		except FileNotFoundError:
			print('Primeiro insira as notas!')
		
		for linha in arq:
				#notas+= linha.split()
				for l in linha:
					notas.append(l)
		d = [None]*(len(notas)-1)
		for i in range(0,len(notas)-1):
			if notas[i] != '\n':
				if notas[i] != '/':
					d[i] = notas[i]
			if notas[i+1] == '/':
				d[i] = notas[i]+notas[i+1]+notas[i+2]
		for j in d:
			if j == None:
				d.remove(j)

		print(d)
		pygame.mixer.init()
		while running == True:
			for n in d:
				print(n)
				
				if len(n)>1:
					#print(n)
					self.juncao_notas(n,len(n))
				elif (n != ' ') and (len(n)==1):
					self.tocar_nota(n)
				elif n== ' ':
					pygame.time.Clock().tick(60)
			break
				
				
			
					
					
					
			self.keyboards()
			self.load_notas()
			pygame.display.flip()
			self.clock.tick(60)

Main_Screen().loop()
