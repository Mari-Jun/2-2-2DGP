from Code import gameframework
from Code.Page import logopage

game = gameframework.Game()
page = logopage.LogoPage(game)

game.run(page)
