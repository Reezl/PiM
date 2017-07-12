import pygame, sys, os

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
	
	def loop(self):
		self.screen = pygame.display.set_mode(self.screen)
		running = True
		
		
		pygame.mixer.init()
		while running == True:
			
			
			
			self.keyboards()
			self.load_notas()
			pygame.display.flip()

Main_Screen().loop()
