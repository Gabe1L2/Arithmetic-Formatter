import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for color, num in args.items():
            for _ in range(num):
                self.contents.append(color)

    def draw(self, num):
        # If you try to draw more balls than available
        if num > len(self.contents):
            random_balls = self.contents.copy()
            self.contents.clear()
            return random_balls
        # make a copy of contents to edit
        random_balls = []
        for _ in range(num):
            random_index = random.randrange(0, len(self.contents))
            # pop the random ball out and append to list
            random_balls.append(self.contents.pop(random_index))
        
        return random_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #hat_contents = copy.copy(hat.contents)
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
            # pop the random ball out and append to list
        random_balls = hat_copy.draw(num_balls_drawn)

        actual_balls = {}
        for item in random_balls:
            # sets dictionary value to 0 if it doesn't exist yet
            actual_balls.setdefault(item, 0)
            actual_balls[item] += 1
        
        good_result = 1
        for exp_key, exp_val in expected_balls.items():
            try:
                if exp_val > actual_balls[exp_key]:
                    good_result = 0
                    break
            except KeyError:
                good_result = 0
        M += good_result
            
    probability = M / num_experiments
    return probability

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(hat3.contents)
print(hat3.draw(2))
print(hat3.contents)
print(probability)