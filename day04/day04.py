input = open("input.txt", "r")
assignment_pairs = input.read().splitlines()
input.close()

def find_overlapping_assignments(assignment_pairs, overlap_type="full"):
    contained_count = 0
    for pair in assignment_pairs:
        assignments = []
        for assignment in pair.split(","):
            list_assignment = assignment.split("-")
            assignments.append(set(range(int(list_assignment[0]), int(list_assignment[1]) + 1)))
        
        if overlap_type == "full":
            if len(assignments[0].intersection(assignments[1])) == len(assignments[0]) or len(assignments[0].intersection(assignments[1])) == len(assignments[1]):
                contained_count += 1
        elif overlap_type == "any":
            if len(assignments[0].intersection(assignments[1])) > 0:
                contained_count += 1
    
    return contained_count

print(find_overlapping_assignments(assignment_pairs))
print(find_overlapping_assignments(assignment_pairs, "any"))