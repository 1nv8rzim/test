import turtle as t

t.speed(0)

# make a square using turtle module

# commands:
#   t.forward(x)    | moves turtle forward x pixels
#   t.backward(c)   | moves turtle backward x pixels
#   t.right(x)      | turns turtle right x degrees
#   t.left(x)       | turns turtle left x degrees


def recursive_square(depth, side_length):
    if depth == 0:
        pass
    else:
        t.fd(side_length)
        recursive_square(depth - 1, side_length / 2)
        t.rt(90)
        t.fd(side_length)
        recursive_square(depth - 1, side_length / 2)
        t.rt(90)
        t.fd(side_length)
        recursive_square(depth - 1, side_length / 2)
        t.rt(90)
        t.fd(side_length)
        recursive_square(depth - 1, side_length / 2)
        t.rt(90)


#recursive_square(5, 100)

color = ['', 'purple', 'blue', 'green', 'yellow', 'orange', 'red']


def recursive_shape(depth, sides, side_length):
    if depth == 0:
        pass
    else:
        for i in range(sides):
            t.color(color[depth])
            t.fd(side_length/sides)
            recursive_shape(depth - 1, sides, side_length/2)
            t.rt(360/sides)


t.pu()
t.rt(90)
t.back(100)
t.lt(90)
t.pd()

recursive_shape(6, 4, 500)


t.done()
