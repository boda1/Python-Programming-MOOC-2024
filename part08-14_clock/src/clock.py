# Write your solution here:

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        elif self.hours != 23 and self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:    
            self.seconds += 1

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

def main():
    clock = Clock(23, 59, 55)
    for i in range(600):
        print(clock)
        clock.tick()

if __name__ == "__main__":
    main()