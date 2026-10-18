import json
import math
import time
from itertools import permutations


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def route_length(order, school, coords):
    """School -> stops in order -> School."""
    points = [school] + [coords[s] for s in order] + [school]
    return sum(dist(points[i], points[i + 1]) for i in range(len(points) - 1))


def brute_force(school, coords):
    best_order, best_len = None, float("inf")
    for order in permutations(coords):                      # (n-1)! orders
        length = route_length(order, school, coords)
        if length < best_len:
            best_order, best_len = order, length
    return list(best_order), best_len


def nearest_neighbor(school, coords):
    current, unvisited, order = school, set(coords), []
    while unvisited:
        nxt = min(unvisited, key=lambda s: dist(current, coords[s]))
        order.append(nxt)
        unvisited.remove(nxt)
        current = coords[nxt]
    return order, route_length(order, school, coords)


def show(title, order, length, seconds):
    print(f"\n{title}")
    print("   Route   : School -> " + " -> ".join(order) + " -> School")
    print(f"   Distance: {length:.2f}   Time: {seconds:.6f} s")


def run(data):
    stops = data["stops"]
    school = (stops[0]["x"], stops[0]["y"])
    coords = {s["name"]: (s["x"], s["y"]) for s in stops[1:]}
    print("\n" + "=" * 60)
    print("PROBLEM 2: DELIVERY ROUTE")
    print("=" * 60)
    print(f"Start/end: {stops[0]['name']} {school}")
    print("Stops    :", coords)

    t = time.perf_counter()
    bf_order, bf_len = brute_force(school, coords)
    t_bf = time.perf_counter() - t

    t = time.perf_counter()
    nn_order, nn_len = nearest_neighbor(school, coords)
    t_nn = time.perf_counter() - t

    show("Simple (brute force)", bf_order, bf_len, t_bf)
    show("Smarter (nearest neighbor)", nn_order, nn_len, t_nn)
    diff = nn_len - bf_len
    if diff > 1e-9:
        print(f"\nNearest neighbor is {diff:.2f} longer than the best route.")
    else:
        print("\nBoth methods found a route of the same length.")


if __name__ == "__main__":
    with open("sample_data.json") as f:
        run(json.load(f)["problem2_delivery_route"])