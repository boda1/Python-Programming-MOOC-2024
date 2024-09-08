# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if self.count_numbers() > 0:    
            return self.get_sum() / self.count_numbers()
        else:
            print("No numbers added")

def main():
    get_input = True
    all_stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    while get_input == True:
        number = int(input("Please provide an integer: "))
        if number == -1:
            get_input = False
        elif number % 2 == 0:    
            all_stats.add_number(number)
            even_stats.add_number(number)
        elif number % 2 != 0:    
            all_stats.add_number(number)
            odd_stats.add_number(number)
        else: 
            get_input = False

    print("Sum of numbers:", all_stats.get_sum())
    print("Mean of numbers:", all_stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Mean of all even numbers:", even_stats.average())
    print("Sum of odd numbers:", odd_stats.get_sum())
    print("Mean of all odd numbers:", odd_stats.average())


main()