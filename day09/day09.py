input = open("input.txt", "r")
rope_movement = input.read().splitlines()
input.close()


def track_rope(rope_movement, knots_num=2):
    knots = []
    for knot in range (0, knots_num):
        knots.append([0, 0])
    
    tail_tracked = []
    # Get the direction and number of steps to take
    for line in rope_movement:
        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        # For each step, move the head one step in the given direction
        for step in range(0, steps):
            match direction:
                case "U":
                    knots[0][1] = knots[0][1] + 1
                case "D":
                    knots[0][1] = knots[0][1] - 1
                case "L":
                    knots[0][0] = knots[0][0] - 1
                case "R":
                    knots[0][0] = knots[0][0] + 1

            # After head has been moved, check if tail needs to be moved.
            for knot_idx in range (1, len(knots)):
                knots[knot_idx] = move_tail(knots[knot_idx - 1], knots[knot_idx])

            # After tail has been potentially moved, check if its current place has already been tracked. If not, add it
            if str(knots[-1]) not in tail_tracked:
                print( knots[-1])
                tail_tracked.append(str(knots[-1]))
    return len(tail_tracked)

# Function tails the head and tail positions as input and checks if tail needs to be moved.
def move_tail(head, tail):
    new_tail = tail
    # Calculate the difference between x,y coordinates between head and tail
    diff = [(head[0] - tail[0]), (head[1] - tail[1])]


    for idx in range(0, len(diff)):
        # For each x/y coordinate, if head is 2 spaces away in either, we know we need to move the tail
        if abs(diff[idx]) > 1:
            # Move tail in the x/y coordinate that is 2 away
            new_tail[idx] = int(new_tail[idx] + (diff[idx] / 2))
            # If x was two away, we need to check that y is the same. If it is not, make it the same
            if idx == 0:
                if abs(diff[1]) == 1:
                    new_tail[1] = new_tail[1] + (diff[1])
            # If y was two away, we need to check that x is the same. If not, make it the same. 
            elif idx == 1:
                if abs(diff[0]) == 1:
                    new_tail[0] = new_tail[0] + (diff[0])
    
    return new_tail

print(track_rope(rope_movement))
print(track_rope(rope_movement, 10))
