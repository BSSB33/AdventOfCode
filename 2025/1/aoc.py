def parse_data(path: str) -> list[str]:
    f = open(path, "r")
    return [n for n in f.read().split("\n")]

def rotate1(value, min_val=0, max_val=100):
    """Wrap a value within a range [min_val, max_val)"""
    range_size = max_val - min_val
    return (value - min_val) % range_size + min_val

def rotate2(start_value, rotation_amount, min_val=0, max_val=100):
    """Count every click that lands on 0 during rotation"""
    range_size = max_val - min_val
    times_at_zero = 0
    current = start_value
    
    if rotation_amount > 0:
        # Rotating right (positive)
        for _ in range(rotation_amount):
            current = (current + 1) % range_size
            if current == 0:
                times_at_zero += 1
    else:
        # Rotating left (negative)
        for _ in range(-rotation_amount):
            current = (current - 1) % range_size
            if current == 0:
                times_at_zero += 1
    
    return current, times_at_zero

def task1(data: list[str]) -> int:
    counter = 0
    value = 50
    for item in data:
        direction = item[0]
        amount = int(item[1:])
        if direction == 'L':
            value = rotate1(value - amount)
        else:
            value = rotate1(value + amount)
        if value == 0:
            counter += 1
    return counter

def task2(data: list[str]) -> int:
    counter = 0
    value = 50
    for item in data:
        direction = item[0]
        amount = int(item[1:])
        if direction == 'L':
            rotation_amount = -amount
        else:
            rotation_amount = amount
        value, times_at_zero = rotate2(value, rotation_amount)
        counter += times_at_zero
    return counter

if __name__ == "__main__":
    data = parse_data("input.txt")
    print(task1(data))
    print(task2(data))