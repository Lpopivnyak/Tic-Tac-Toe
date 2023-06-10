import pygame
import time

class Card:
    def __init__(self, x, y, w, h, text, borderColor, insideColor):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.borderColor = borderColor
        self.insideColor = insideColor
        self.borderRect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.insideRect = pygame.Rect(self.x+10, self.y+10, self.w-20, self.h-20)
        self.renderText = pygame.font.Font(None, 36).render( self.text, True, (0, 0, 0))
    def render(self, window):
        pygame.draw.rect(window,  self.borderColor, self.borderRect)
        pygame.draw.rect(window, self.insideColor, self.insideRect)
        screen.blit( self.renderText, [self.x+35, self.y+20])

    def changetext(self, text):
        self.text = text
        self.renderText = pygame.font.Font(None, 72).render( self.text, True, (0, 0, 0))




pygame.init()

screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()
pole = []
pole.append(Card(100, 50, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(200, 50, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(300, 50, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(100, 150, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(200, 150, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(300, 150, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(100, 250, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(200, 250, 100, 100, "", (0, 0, 0), (198, 245, 234)))
pole.append(Card(300, 250, 100, 100, "", (0, 0, 0), (198, 245, 234)))
first = 1

winText = pygame.font.Font(None, 56).render("Гравець 1 Виграв!", True, (255, 0, 0))
loseText = pygame.font.Font(None, 56).render("Гравець 2 Виграв!", True, (255, 0, 0))
drawText = pygame.font.Font(None, 56).render("Нічия!", True, (255, 0, 0))
winTimeText = pygame.font.Font(None, 56).render("Думай головоою швидше Гравець 2.Гравець 1 Виграв!", True, (255, 0, 0))
starttime = time.time()
sec = 5-(time.time() - starttime)
timeText = pygame.font.Font(None, 56).render("Час:" + str(sec), True, (255, 0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(9):
                if pole[i].borderRect.collidepoint(x, y):
                    if pole[i].text == "":
                        starttime = time.time()
                        if first%2 == 0:
                            pole[i].changetext("O")
                            first += 1
                        else:
                            pole[i].changetext("X")
                            first += 1

    sec = 5-(time.time() - starttime)
    timeText = pygame.font.Font(None, 56).render("Час:" + str(round(sec)), True, (255, 0, 0))
    if sec <= 0:
        if first%2 == 1:
            screen.blit(loseTimeText,[120,400])
            pygame.display.flip()
            break
        else:
            screen.blit(winTimeText,[70,400])
            pygame.display.flip()
            break

    screen.fill((198, 245, 234))
    for i in range(9):
        pole[i].render(screen)
    screen.blit(timeText,[0, 0])
    pygame.display.flip()
    if pole[0].text == "X" and pole[1].text == "X" and pole[2].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (130, 95), (373, 95), 5)
       screen.blit(winText,[120,400])
       pygame.display.flip()
       break
    if pole[3].text == "X" and pole[4].text == "X" and pole[5].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (130, 195), (373, 195), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[6].text == "X" and pole[7].text == "X" and pole[8].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (130, 295), (373, 295), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[0].text == "X" and pole[3].text == "X" and pole[6].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (153, 65), (153, 325), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[1].text == "X" and pole[4].text == "X" and pole[7].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (253, 65), (253, 325), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[2].text == "X" and pole[5].text == "X" and pole[8].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (353, 65), (353, 325), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[0].text == "X" and pole[4].text == "X" and pole[8].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (130, 70), (380, 320), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[2].text == "X" and pole[4].text == "X" and pole[6].text == "X":
       pygame.draw.line(screen, (0, 0, 0), (370, 72), (130, 315), 5)
       screen.blit(winText,[120, 400])
       pygame.display.flip()
       break
    if pole[0].text == "O" and pole[1].text == "O" and pole[2].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (130, 95), (373, 95), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[3].text == "O" and pole[4].text == "O" and pole[5].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (130, 195), (373, 195), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[6].text == "O" and pole[7].text == "O" and pole[8].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (130, 295), (373, 295), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[0].text == "O" and pole[3].text == "O" and pole[6].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (153, 65), (153, 325), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[1].text == "O" and pole[4].text == "O" and pole[7].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (253, 65), (253, 325), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[2].text == "O" and pole[5].text == "O" and pole[8].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (353, 65), (353, 325), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[0].text == "O" and pole[4].text == "O" and pole[8].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (130, 70), (380, 320), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if pole[2].text == "O" and pole[4].text == "O" and pole[6].text == "O":
       pygame.draw.line(screen, (0, 0, 0), (370, 72), (130, 315), 5)
       screen.blit(loseText,[120, 400])
       pygame.display.flip()
       break
    if first == 10:
        screen.blit(drawText,[210, 400])
        pygame.display.flip()
        break

    fps.tick(60)
