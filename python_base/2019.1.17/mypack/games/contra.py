def play() :
    print('正在玩魂斗罗')
def gameover() :
    print('游戏结束')
    from ..menu import show_menu
    show_menu()
def tanks() :
    from .tanks import play
    play()
print('魂斗罗模块正在被加载')