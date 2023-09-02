from itertools import combinations
from math import sqrt, inf

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_profit_and_blimps(route, cost_per_mile, decline_factor, cities_per_decline):
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

def solve_blimp_sales_with_blimps(c, d, cities):
    best_profit = -inf
    best_route = []
    
    cities_per_decline = len(cities)
    
    for r in range(1, len(cities) + 1):
        for route in combinations(cities, r):
            profit, blimps = calculate_profit_and_blimps(route, c, d, cities_per_decline)
            if profit > best_profit:
                best_profit = profit
                best_route = route
    
    return best_profit, best_route

def main():
    n, c, d = map(float, input().split())
    cities = [tuple(map(int, input().split())) for _ in range(int(n))]
    
    best_profit, best_route = solve_blimp_sales_with_blimps(c, d, cities)
    
    current_x, current_y = 0, 0
    blimps_to_take = len(best_route)
    
    for x, y, _ in best_route:
        print(f"{x} {y} {blimps_to_take}")
        blimps_to_take -= 1
        current_x, current_y = x, y

if __name__ == '__main__':
    main()
