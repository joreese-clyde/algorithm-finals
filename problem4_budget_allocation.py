import json
import time
from itertools import combinations


def brute_force(items, budget):
    best, best_score = [], 0
    for r in range(len(items) + 1):
        for combo in combinations(items, r):                # 2^n combinations
            cost = sum(i["cost"] for i in combo)
            score = sum(i["score"] for i in combo)
            if cost <= budget and score > best_score:
                best, best_score = list(combo), score
    return best


def greedy(items, budget):
    ordered = sorted(items, key=lambda i: i["score"] / i["cost"], reverse=True)
    chosen, spent = [], 0
    for item in ordered:
        if spent + item["cost"] <= budget:                  # take it only if it fits
            chosen.append(item)
            spent += item["cost"]
    return chosen


def show(title, chosen, budget, seconds):
    print(f"\n{title}")
    for i in chosen:
        print(f"   {i['name']:<13} cost={i['cost']:<3} score={i['score']}")
    print(f"   Total score: {sum(i['score'] for i in chosen)}   "
          f"Money used: {sum(i['cost'] for i in chosen)}/{budget}   Time: {seconds:.6f} s")


def run(data):
    budget, items = data["budget"], data["items"]
    print("\n" + "=" * 60)
    print("PROBLEM 4: BUDGET ALLOCATION")
    print("=" * 60)
    print("Budget:", budget)
    print("Items :")
    for i in items:
        print(f"   {i['name']:<13} cost={i['cost']:<3} score={i['score']}")

    t = time.perf_counter()
    bf = brute_force(items, budget)
    t_bf = time.perf_counter() - t

    t = time.perf_counter()
    gr = greedy(items, budget)
    t_gr = time.perf_counter() - t

    show("Simple (brute force)", bf, budget, t_bf)
    show("Smarter (greedy by score/cost)", gr, budget, t_gr)


if __name__ == "__main__":
    with open("sample_data.json") as f:
        run(json.load(f)["problem4_budget_allocation"])