from turtle import *
 
def dragon(level, size, direction=45):
    if level:
        right(direction)
        dragon(level-1, size/(2**.5), 45)
        left(direction * 2)
        dragon(level-1, size/(2**.5), -45)
        right(direction)
    else:
        forward(size)

if __name__ == "__main__":
    speed(0)
    hideturtle()
    dragon(12, 200)
    exitonclick()
