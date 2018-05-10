========README========
This program is edited by childishmori(Github) who is a complete beginner in game programming.
This is an open source program and needs python environment to run.
It is not available for commercial use.
And do not forget to mention me when use this program in other ways.

The icon and background music are found on the internet.
If there is any problems about the copyright of these, please contact me.

The Assists dictionary contains every assistant class such as GameOver to show the game over  interface.
The Enemies dictionary contains every class relating to the enemies.
The Environment dictionary contains only the Stars class to build space environment.
The Icon dictionary contains only the icon of this program.
The Music dictionary contains only the background music of this game.
The Play dictionary contains every class that relates to the player's ship.
And at last, the Promotion dictionary contains only the DiffSpeed class, which is not used in any other python files.
It has the same ability like the class Speed, but is built with friction and inertia.
It is more natural than the Speed class, but will bring an unpleasant experience.
So if you'd like to enjoy this, please change the Player/Ship line 3:
    'from Assists.Speed import Speed' to 'from Promotion.DiffSpeed import Speed'.

To play this game, please run the Main.py and use your keyboard to control your ship.
Your ship is the letter 'A' and your bullets are '^'.
Your enemies are the letter 'o' and their bullets are 'v'.
Your HP is at the top left corner and your points is at the top right corner.
You need to shot enemies to get points while avoid your crash.
You can use WASD or Arrow Keys to move your ship.
You can shot with the key J.
Space is used to stop the game, and ESC is used to exit this program.
A crashed enemy will give you 2 points.
And an enemy who successfully escaped will take 1 point away.

So just enjoy yourself playing this game.

I am too tired to make any addition or deletion to this program now.
So if you find any bug while play, please contact me or leave a message.
I will change them in the next version, if time permits.
Any sincere suggestions are welcome.
And I am so grateful that you are willing to play my game.
========childishmori========
========2018/5/11========
