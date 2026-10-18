import json
import os
 
import problem1_exam_scheduling as p1
import problem2_delivery_route as p2
import problem4_budget_allocation as p4
 
if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data.json")
    with open(path) as f:
        data = json.load(f)
 
    print("algorithm showdown: simple vs smarter algorithms")
    print("my chosen problems: 1 (exam scheduling), 2 (delivery route), 4 (budget allocation)")
    p1.run(data["problem1_exam_scheduling"])
    p2.run(data["problem2_delivery_route"])
    p4.run(data["problem4_budget_allocation"])
 