input = open("input.txt", "r")
trees = input.read().splitlines()
input.close()

def count_visible_trees(trees):
    visible_count = 0


    spotted = []
    best_scenic = 0
    for idx_row in range(1, len(trees) - 1):
        for idx_col in range(1, len(trees[idx_row]) - 1):
            tree = trees[idx_row][idx_col]
            tallest = [1, 1, 1, 1]
            scenic  = [0, 0, 0, 0]
            scenic_done = [False, False, False, False]
            # Check up
            for idx_y in range(idx_row -1, -1, -1):
                scenic[0] = scenic[0] + 1
                if trees[idx_y][idx_col] >= tree:
                    tallest[0] = 0
                    scenic_done[0] = True
                    break
                        
            # Check down
            for idx_y in range(idx_row + 1, len(trees)):
                scenic[1] = scenic[1] + 1
                if trees[idx_y][idx_col] >= tree:
                    tallest[1] = 0
                    scenic_done[1] = True
                    break
                       
            # Check left
            for idx_x in range(idx_col -1, -1, -1):
                scenic[2] = scenic[2] + 1
                if trees[idx_row][idx_x] >= tree:
                    tallest[2] = 0
                    scenic_done[2] = True
                    break
                        
            # check right
            for idx_x in range(idx_col + 1, len(trees[idx_row])):
                scenic[3] = scenic[3] + 1
                if trees[idx_row][idx_x] >= tree:
                    tallest[3] = 0
                    scenic_done[3] = True
                    break
            
            scenic_score = 1
            for score in scenic:
                scenic_score *= score

            if scenic_score > best_scenic:
                best_scenic = scenic_score

            if 1 in tallest:
                spotted.append(trees[idx_row][idx_col])
                visible_count += 1

    visible_count += (len(trees[0]) * 4) - 4

    return visible_count, best_scenic



print(count_visible_trees(trees))