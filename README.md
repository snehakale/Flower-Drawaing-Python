## Project Title
### Flower Drawing Python Program
This is a python program which draws a flower by making use of *turtle* library.

## Pre-Requisites and Installation
1. Download the project.
2. Download [Python](https://www.python.org/downloads/).
3. Install python step-by-step on your machine. Refer these links, for [windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) and for [Mac](https://docs.python.org/3/using/mac.html)
4. Run **draw_flower.py**.

## Code Examples
In draw_flower.py file :
1) `import turtle` to import turtle library in order to draw shapes
2) `def draw_rectangle(some_turtle) ...` function draws a rectangle for a given turtle object.
3) `def draw_flower():... ` function draws a flower.
    Inside that, there is a statement ` window = turtle.Screen()` to get a screen / canvas to draw flower. 
    Then it creates `flower = turtle.Turtle()
    flower.shape("circle") ... ` , a turtle object with its defined properties like shape, color etc.
    Then it calls function `draw_rectangle(flower)` to draw a rectange at given point in a loop.

## References 
1. [Python Documentation](https://docs.python.org/3/)
2. [Python Turtle Library](https://docs.python.org/2/library/turtle.html)

## Author 
Sneha Kale