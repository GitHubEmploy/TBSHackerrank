from itertools import combinations
from math import sqrt, inf

# Function to calculate distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_profit_and_blimps(route, city_data, cost_per_mile, decline_factor, cities_per_decline):
    total_distance = 0
    total_sales = 0
    total_blimps_cost = 0
    blimps_to_take = len(route)
    
    current_x, current_y = 0, 0  # Starting at the headquarters
    
    for i, (x, y, price) in enumerate(route):
        dist = distance(current_x, current_y, x, y)
        total_distance += dist  # Update total distance
        total_blimps_cost += dist * blimps_to_take  # Update total blimps cost
        
        # Apply decline factor
        if (i + 1) % cities_per_decline == 0:
            price *= decline_factor
            
        total_sales += price  # Update total sales
        
        current_x, current_y = x, y  # Update current position
        blimps_to_take -= 1  # Decrease remaining blimps
    
    # Calculate total cost and profit
    total_cost = total_distance * cost_per_mile + total_blimps_cost * cost_per_mile
    total_profit = total_sales - total_cost
    
    return total_profit, len(route)

# Function to solve the problem with blimp count
def solve_blimp_sales_with_blimps(c, d, cities):
    best_profit = -inf
    best_route = []
    best_blimps = 0
    
    cities_per_decline = len(cities)  # As per the problem description
    
    # Generate all combinations of routes (this will be feasible only for small inputs)
    for r in range(1, len(cities) + 1):
        for route in combinations(cities, r):
            profit, blimps = calculate_profit_and_blimps(route, cities, c, d, cities_per_decline)
            if profit > best_profit:
                best_profit = profit
                best_route = route
                best_blimps = blimps
    
    # Generate output
    output = []
    current_x, current_y = 0, 0
    first_city = True
    for x, y, _ in best_route:
        if first_city:
            output.append((x, y, best_blimps))
            first_city = False
        else:
            output.append((x, y))
        current_x, current_y = x, y
    
    return best_profit, output

def tbsp(c, d, cities):
    best_profit, best_route_with_blimps = solve_blimp_sales_with_blimps(c, d, cities)
    for x, y, *blimps in best_route_with_blimps:
        if blimps:
            print(f"{x} {y} {blimps[0]}")
        else:
            print(f"{x} {y}")    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    c = float(first_multiple_input[1])

    d = float(first_multiple_input[2])

    cities = []

    for _ in range(n):
        cities.append(list(map(int, input().rstrip().split())))

    tbsp(c, d, cities)
