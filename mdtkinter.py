from tkinter import *

class App:
	def __init__(self, master=None):
		master.geometry('400x400')
		master.title('PiM')
		master.iconbitmap('PiM.ico')
		mycolorP = self.colors(50,50,50)
		master.tk_setPalette(background=mycolorP,activeForeground='#ffffff')
		#master['bg'] = mycolorP
		
		self.titulo = Label(master,text="Insira suas notas: ")#,bg=mycolorP,fg='white'
		self.titulo["font"] = ('Arial','10','bold')
		self.titulo.pack()
		
		
		mycolor = self.colors(80,80,80)
		self.t = Text(master, width=40, height = 20,bg=mycolor)
		self.t.pack()
		
		self.ok = Button(master,text='OK',font=('Arial',10))#bg=mycolorP,fg='white',
		self.ok.bind('<Button-1>',self.gerar_notas)
		self.ok.pack()
	
	def gerar_notas(self,event):
		notas = open('notas.txt','w')
		notas.write(str(self.t.get('1.0','end-1c')))
	def colors(self,r,g,b):
		mycolor = '#%02x%02x%02x' % (r, g, b)
		return mycolor


'''
class App:
	def __init__(self, master=None):
		self.widgets = Frame(master)
		self.widgets.pack()
		
		self.notas = Label(self.widgets,text="Notas:")
		self.notas.pack(side=LEFT)
		

		self.ok = Button(self.widgets)
		self.ok["text"] = "Sair"
		self.ok["font"] = ("Fixedsys", "8")
		self.ok["width"] = 5
		#self.ok["command"] = self.widgets.quit #sys.exit
		self.ok["bg"] = 'white'
		self.ok["fg"] = "black"
		self.ok["command"] = self.mudarTexto
		#self.ok.bind("<Button-1>",self.mudarTexto)
		self.ok.pack(side=RIGHT)
	
	def mudarTexto(self): # if bind args + event
		print("Clicado")
		

'''

root = Tk()
if __name__ == "__main__":
	App(root)
	root.mainloop()
