import pygame
 
pygame.init() #Programı çalıştırmdık.

boyut = (900,600) #Oyunun boyutlarını belirledik.

top = pygame.image.load("keko.png")



TopX =  top.get_size()[0]
topY =  top.get_size()[1]


pencere = pygame.display.set_mode(boyut) #Oyunumuz'daki kullanacağımız özelikleri ekrana yazdıracağız.

x = 0 
y = 0
xYon = 1
yYon = 1

clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    if x > 900 - TopX or x < 0:
        xYon *= -1
    
    if y > 600  - topY or y < 0:
        yYon *= -1
        
    pencere.fill((255,255,255)) #Arkadaki alanı belirtilen renk yaptık.
    x += 6 * xYon
    y += 6 * yYon
    pencere.blit(top,(x,y))
    pygame.display.update()
    
    

