from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    segments = []
    def create_segment(self, segments):
        segment = Turtle("square")
        segment.color("white")
        segment.speed(1)
        segment.up()

        if (segments == []):
            position = (0, 0)
        else:
            tail_x = segments[-1].xcor()
            tail_y = segments[-1].ycor()
            position = (tail_x, tail_y)
        segment.goto(position)

        return segment

    def initialize_segments(self):
        segments = []
        for i in range(3):
            segment = self.create_segment(segments)
            segments.append(segment)
        return segments

    def __init__(self):
        self.reset_snake()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments = self.initialize_segments()
        self.head = self.segments[0]
