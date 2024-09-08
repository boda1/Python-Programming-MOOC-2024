# Write your solution here

def average(person: dict):
    keys = ["result1", "result2", "result3"]
    avg = sum([person[key] for key in keys]) / len(keys)

    return avg

def smallest_average(person1: dict, person2: dict, person3: dict):    
    person1_mean = average(person1)
    person2_mean = average(person2)
    person3_mean = average(person3)

    min_avg = min([person1_mean, person2_mean, person3_mean])

    if person1_mean == min_avg:
        return person1
    elif person2_mean == min_avg:
        return person2
    else:
        return person3
    
def main():
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print("hello")
    smallest_average()


if __name__ == "__main__":
    main()