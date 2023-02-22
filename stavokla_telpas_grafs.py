import random

# this code represents P2 side of the problem 

list_choices = []
i = 0
# at the beginning three choices for who can cross, after that, two choices, when going back also two choices 
possible_iterations = 3 * 2 * 2

while i < possible_iterations:

    letter_first = random.choice(["A", "B", "C"])

    if letter_first == "A":
        letter_two = random.choice(["B", "C"])
        letter_three = random.choice(["A", letter_two])
    if letter_first == "B":
        letter_two = random.choice(["A", "C"])
        letter_three = random.choice(["B", letter_two])
    if letter_first == "C":
        letter_two = random.choice(["A", "B"])
        letter_three = random.choice(["C", letter_two])

    letter_string = letter_first + letter_two + letter_three

    if letter_string in list_choices:
        continue
    else:
        list_choices.append(letter_string)
        i = i + 1

class Node: # modificēts no https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree.py#L4

    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def children_add(self, child):
        child.parent = self
        self.children.append(child)

    def draw_tree_structure(self):
        iteration = 0
        pre_parent = self.parent
        while pre_parent:
            iteration = iteration + 1
            pre_parent = pre_parent.parent
        return iteration

    def print_tree(self):
        lines_draw = '   ' * self.draw_tree_structure() + "|--"
        if self.parent:
            pass
        else: 
            ""
        print(lines_draw + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():

    print("SIDE P2")

    time_start = 12
    root = Node("EMPTY" + " (time: "+ str(time_start)+ ")")
    temp_storage = []

    for letter_string in list_choices:
        first_bridge_crossers = ""
        for letter in letter_string:
            time_after_first_cross = time_start

            if len(first_bridge_crossers) < 2:
                first_bridge_crossers = first_bridge_crossers + letter
                continue
            elif first_bridge_crossers in temp_storage:
                continue
            elif first_bridge_crossers == "CA":
                continue
            elif first_bridge_crossers == "CB":
                continue
            elif first_bridge_crossers == "BA":
                continue
            else:
                temp_storage.append(first_bridge_crossers)

                if first_bridge_crossers.__contains__("A") and first_bridge_crossers.__contains__("B"):
                    time_after_first_cross = time_after_first_cross - 3
                elif first_bridge_crossers.__contains__("B") and first_bridge_crossers.__contains__("C"):
                    time_after_first_cross = time_after_first_cross - 5
                elif first_bridge_crossers.__contains__("A") and first_bridge_crossers.__contains__("C"):
                    time_after_first_cross = time_after_first_cross - 5
                
                first_iteration_of_tree = Node(first_bridge_crossers + " (time: "+ str(time_after_first_cross)+ ")")

                for alone_bridge_crosser in list_choices:
                    time_after_second_cross = time_after_first_cross
                    if first_bridge_crossers == alone_bridge_crosser[0] + alone_bridge_crosser[1]:
                        second_iteration_of_tree = alone_bridge_crosser[2]

                        cross_time_map_alone_crosser = {
                            ("AB", "A"): 3, ("AC", "A"): 5, ("BC", "B"): 5, ("AB", "B"): 1, ("AC", "C"): 1, ("BC", "C"): 3,
                            ("BA", "A"): 3, ("CA", "A"): 5, ("CB", "B"): 5, ("BA", "B"): 1, ("CA", "C"): 1, ("CB", "C"): 3
                        }

                        for stayer in second_iteration_of_tree:
                            if (first_bridge_crossers, stayer) in cross_time_map_alone_crosser:
                                time_after_second_cross -= cross_time_map_alone_crosser[(first_bridge_crossers, stayer)]

                        second_iteration_of_tree_assing = Node(second_iteration_of_tree  + " (time: "+ str(time_after_second_cross)+ ")")
                        time_after_third_cross = time_after_second_cross

                        if second_iteration_of_tree.__contains__("A"):
                            time_after_third_cross = time_after_third_cross - 5
                        elif second_iteration_of_tree.__contains__("B"):
                            time_after_third_cross = time_after_third_cross - 5
                        elif second_iteration_of_tree.__contains__("C"):
                            time_after_third_cross = time_after_third_cross - 3
                        
                        if time_after_third_cross > 0:
                            end = Node("ABC" + " (time: "+ str(time_after_third_cross)+ ")")

                        first_iteration_of_tree.children_add(second_iteration_of_tree_assing)
                        
                        if time_after_third_cross > 0:
                            second_iteration_of_tree_assing.children_add(end)

                        alone_bridge_crosser = "0"

                root.children_add(first_iteration_of_tree)
    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()

