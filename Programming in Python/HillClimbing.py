##Hill Climbing Algorithm
def objective_function(x):
    return -(x**2) + 10*x
def hill_climbing(start):
    current = start
    step = 1
    current_value = objective_function(current)
    print(f"Starting hill climbing from x = {current} with f(x) = {current_value}")
    while True:
        next_value = objective_function(current + step)
        print(f"Checking right neighbor at x = {current + step} with f(x) = {next_value}")
        if next_value > current_value:
            current += step
            current_value = next_value
            print(f"Moving to x = {current} with f(x) = {current_value}")
        else:
            next_value = objective_function(current - step)
            print(f"Checking left neighbor at x = {current - step} with f(x) = {next_value}")
            if next_value > current_value:
                current -= step
                current_value = next_value
                print(f"Moving to x = {current} with f(x) = {current_value}")
            else:
                print("No further improvement, stopping search.")
                break
    return current
start = 0
result = hill_climbing(start)
print(f"Maximum value found at x = {result}")