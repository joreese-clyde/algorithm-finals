import json
import time
from itertools import product


def brute_force(exams, conflicts):
    """Try 1 slot, then 2, then 3... every possible assignment; first valid = fewest slots."""
    n = len(exams)
    index = {e: i for i, e in enumerate(exams)}
    for k in range(1, n + 1):
        for combo in product(range(k), repeat=n):          # every assignment
            if all(combo[index[a]] != combo[index[b]] for a, b in conflicts):
                slots = [[] for _ in range(k)]
                for exam, s in zip(exams, combo):
                    slots[s].append(exam)
                return slots


def greedy(exams, conflicts):
    """Take exams one at a time; put each in the first slot with no conflict."""
    pairs = {frozenset(c) for c in conflicts}
    slots = []
    for exam in exams:
        for slot in slots:
            if not any(frozenset((exam, other)) in pairs for other in slot):
                slot.append(exam)
                break
        else:
            slots.append([exam])                            # no slot fit -> open a new one
    return slots


def print_table(title, slots, seconds):
    print(f"\n{title}  ->  {len(slots)} slots, time = {seconds:.6f} s")
    for i, slot in enumerate(slots, 1):
        print(f"   Slot {i}: {', '.join(slot)}")


def run(data):
    exams, conflicts = data["exams"], data["conflicts"]
    print("=" * 60)
    print("PROBLEM 1: EXAM SCHEDULING")
    print("=" * 60)
    print("Exams    :", exams)
    print("Conflicts:", conflicts)

    t = time.perf_counter()
    bf = brute_force(exams, conflicts)
    t_bf = time.perf_counter() - t

    t = time.perf_counter()
    gr = greedy(exams, conflicts)
    t_gr = time.perf_counter() - t

    print_table("Simple (brute force)", bf, t_bf)
    print_table("Smarter (greedy)", gr, t_gr)
    if len(gr) > len(bf):
        print(f"\nNote: greedy used {len(gr) - len(bf)} extra slot(s) - faster but not optimal.")
    else:
        print("\nNote: both methods used the same number of slots.")


if __name__ == "__main__":
    with open("sample_data.json") as f:
        run(json.load(f)["problem1_exam_scheduling"])