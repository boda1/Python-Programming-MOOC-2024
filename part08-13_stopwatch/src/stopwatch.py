# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.minutes == 59 & self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
        elif self.minutes != 59 & self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:    
            self.seconds += 1

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

def main():
    watch = Stopwatch()
    for i in range(600):
        print(watch)
        watch.tick()

if __name__ == "__main__":
    main()