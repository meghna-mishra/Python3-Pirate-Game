import pygame
import random
pygame.init()

#Some colors
blue=(100,149,237)
green=(69,139,116)
black=(0,0,0)
white=(255,255,255)
carry=True

#font
font_name="ostrich-regular.ttf"

#player class
class Players(pygame.sprite.Sprite):
  def __init__(self,imagein):
   super().__init__()
   self.image=pygame.image.load(imagein).convert_alpha()
   self.rect=self.image.get_rect()
  def moveright(self, pixels):
  	self.rect.x+=pixels
  def moveleft(self,pixels):
  	self.rect.x-=pixels
  def moveup(self,pixels):
  	self.rect.y-=pixels
  def movedown(self,pixels):
  	self.rect.y+=pixels

#obstacle class
class Obstacles(pygame.sprite.Sprite):
  def __init__(self,imagein):
   super().__init__()
   self.image=pygame.image.load(imagein).convert_alpha()
   self.rect=self.image.get_rect()

#update function to control speed
def update(self,speed):
	self.rect.x+=speed
	if self.rect.x>700:
		self.rect.x=0
