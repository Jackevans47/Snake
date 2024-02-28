# My Snake Game

![Responsive](https://github.com/Jackevans47/Snake/assets/148341732/93829c86-906a-48b8-a0f9-670a24bde6aa)

*The link to [My Snake Game](https://snake-3.onrender.com/)*

My Snake Game is a python terminal project that allows users to be able to play the classic snake game via terminal.

Users can quickly learn the rules and jump straight into the game.

---

## How to play:

  1. Click this *[link](https://snake-3.onrender.com/)* or copy this text: `https://snake-3.onrender.com/` and paste it in your browser's address bar.
  1. As soon as the page has loaded, you will be presented with 3 options. 'Play', 'Rules', 'Exit'
  1. 'Play' will run the game. 'Rules' will show the user the rules to the game. 'Exit' will close the program.
  1. When the game is active, control the snake to eat the fruit without hitting itself or the walls.
  1. If the food is eaten, the snake will increase in size and a point will be added to the score.
  1. If the snake eats itself or hits the wall, a game over message will appear where the user can see their score.
  1. An option is presented to the user to return them to the menu.

  Link to the game: *https://snake-3.onrender.com/*   

---
## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the games primary purpose so that I can enjoy playing it.
* As a First Time Visitor, I want to navigate through the game easily so that I can have fun playing.
* As a First Time Visitor, I want to be able to find out the rules so i know how to play.

### Frequent Visitor Goals:
* As a Frequent User, I want to be able to challenge myself to beat my previous score.
* As a Frequent User, I want the placement of the food to be randomised so the game remains interesting. 

---

## Features
  
  - **When the game is loaded**

    The user can see a menu with 3 options.
    
    - Shows the terminal menu with three options:

    1. Play
    2. Rules
    3. Exit
   
    ![main menu](https://github.com/Jackevans47/Snake/assets/148341732/fc37ccfd-2e0d-4fe2-85f4-804c0b3f11da)

The user can interact with the menu with the arrowkeys to choose an option then hit enter to confirm.

 - **When the user chose "Play"**

   The program will begin to run and the user can play the game.
   
   ![game run](https://github.com/Jackevans47/Snake/assets/148341732/8b8cb381-d38b-4a5e-b56a-630d729f5843)

   
 - **When the user chose "Rules"**

   The rules are explained to the user with a return key below directing the user back to the main menu.

   ![rules message](https://github.com/Jackevans47/Snake/assets/148341732/c18adad1-d076-4eb8-a461-8608077f2e77)


   - **When the user chose "Exit"**
  
   The program will close and the user is shown an exit message confirming they have quit the game.

   ![exit game message](https://github.com/Jackevans47/Snake/assets/148341732/08aaea17-9305-47bc-97cc-4bbc48fc0b6e)

  - **When the user scores a point**

    When the user eats the food and scores a point, the snake size is increased by 1 and a point is added.

    ![snake increase size](https://github.com/Jackevans47/Snake/assets/148341732/d387312f-6ad5-43e7-a2b6-80d7a3fa9582)
    
    ![score](https://github.com/Jackevans47/Snake/assets/148341732/f0164467-7a1f-4ccf-9d42-dc0f6bad28b1)

   - **When the user hits the wall or the snake**

     When the user hits the boundaries on the game are or collides with the snake, a game over message will pop up on screen showing the user the game is over.

     ![snake eats itself](https://github.com/Jackevans47/Snake/assets/148341732/5ee2ae0f-47b6-482a-ac60-05af606fdc50)


     A message will appear telling the user to press any key to be returned to the menu.

     ![game over](https://github.com/Jackevans47/Snake/assets/148341732/cdd28d5a-ff7a-473f-9f5e-b010b61c2692)
     
---

## Flowchart

The flowchart represents the logic of the application:

  <img width="555" alt="flow chart" src="https://github.com/Jackevans47/Snake/assets/148341732/6beb9220-0e99-4b3e-a17d-5ca2dd66fa2e">


---
## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-396/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program.
##### Third-party imports:
- [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/) was used to implement the menu.
- [cursor](https://pypi.org/project/cursor/) was used to implement the controls for the game.

#### Other tools:
- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [render.com](https://render.com/) was used to deploy the project.
- [Draw.io](https://app.diagrams.net/) was used to make a flowchart for the README file.


---
