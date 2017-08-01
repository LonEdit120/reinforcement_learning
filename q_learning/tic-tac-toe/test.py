import train
import circle
import cross
import shutdown
import random

train.clearMap()
game = train.getGame()
train.defPlace('O',0,game)
game = train.getGame()
train.defPlace('O',2,game)
game = train.getGame()
train.defPlace('O',4,game)
game = train.getGame()
train.defPlace('O',7,game)
game = train.getGame()
train.defPlace('O',8,game)
game = train.getGame()

print (game)
b = shutdown.detect('O', game)
lst = shutdown.getShutDownPos()
print(b)
print(lst)
