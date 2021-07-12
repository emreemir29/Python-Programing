import pygame

 
pygame.init() #Programı çalıştırmdık.

boyut = (900,600) #Oyunun boyutlarını belirledik.

top = pygame.image.load("top.png")

pygame.mouse.set_visible(0)

TopX =  top.get_size()[0]
topY =  top.get_size()[1]


pencere = pygame.display.set_mode(boyut) #Oyunumuz'daki kullanacağımız özelikleri ekrana yazdıracağız.

x = 0 
y = 0

clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.mouse.get_pos()
        
    pencere.fill((255,255,255)) #Yazı her geçtiği zaman arkadaki alanı belirtilen renk yaptık.

    mouseX, MouseY = pygame.mouse.get_pos()
    
    if mouseX + top.get_size() [0] > 800:
        mouseX = mouseX - top.get_size() [0]
    
    elif MouseY + top.get_size() [1] > 600:
        MouseY = MouseY - top.get_size()[1]
    
    pencere.blit(top, (mouseX,MouseY))
    
    pygame.display.update()
    