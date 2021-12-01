from string import ascii_lowercase

groups = open('input.txt').read().split('\n\n')
groups = [group.split('\n') for group in groups]
merged_groups = ["".join(group) for group in groups]

def getSumOfYes():
    unique_groups = []
    for group in merged_groups:
        unique_chars = set()
        for char in group:
            unique_chars.add(char)
        unique_groups.append(unique_chars)
    return [sum([len(group) for group in unique_groups])][0]
    

def getSumOfAllYes():
    sum_of_same_yes = 0
    for group in groups:
        for c in ascii_lowercase:
            if all(c in person for person in group):
                sum_of_same_yes += 1

    return sum_of_same_yes
    
if __name__ == "__main__":
    print("Sum of 'Yes' in Groups: " + str(getSumOfYes()))
    print("Sum of Only 'Yes' in Groups: " + str(getSumOfAllYes()))
