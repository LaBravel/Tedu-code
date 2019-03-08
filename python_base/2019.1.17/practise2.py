#此主模块的作用是测试mypack/games/contra.py里的gameover函数的相对导入
import mypack.games.contra as c
c.gameover()
print('程序退出')