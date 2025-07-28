import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO 1: Create snake, food, scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# TODO 3: Control the snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    # TODO 2: Move the snake
    snake.move()

    # TODO 4: Detect collision with the food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    # TODO 5: Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # TODO 6: Detect collision with tail
    # for segment in snake.snake_body:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
