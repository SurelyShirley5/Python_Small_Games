from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position=position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("lightgreen")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for i in self.snake_body:
            i.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for segment_ind in range(len(self.snake_body) - 1, 0, -1):
            new_position = self.snake_body[segment_ind - 1].position()
            self.snake_body[segment_ind].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
