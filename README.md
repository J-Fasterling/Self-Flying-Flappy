FlappyBirdClone by [xiaomomo](https://github.com/xiaomomo/FlappyBirdClone)
===============

A Flappy Bird Clone made using [python-pygame][1]

How to run basic FlappyBirdClone
------

1. Install Python 2.7.X or 3.5.x from [here](https://www.python.org/download/releases/)

2. Install PyGame 1.9.X from [here](http://www.pygame.org/download.shtml)

3. Clone this repository: `git clone https://github.com/sourabhv/FlappyBirdClone.git` or click `Download ZIP` in right panel and extract it.

4. Run `python flappy.py` from the repo's directory

5. use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

  (Note: Install pyGame for same version python as above)

  (For x64 windows, get exe [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame))

ScreenShot
----------

![Flappy Bird](screenshot1.png)

[1]: http://www.pygame.org

How to train Self Flying Flappy
----------
1. Install all dependencies 

2. Adjust save_step parameter to desired step you want to save

3. Run ./train_Flappy/q-learning.py

How to use Self Flying Flappy
----------
1. Install all dependencies 

2. Change name of .pickle file you want to use in ./Q-Values/ to Q.pickle

3. Run ./use_Flappy/use_q-learning.py

