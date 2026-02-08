class FrequencyTracker:
    def __init__(self):
        self.freq = {}
        self.count = {}

    def add(self, number: int) -> None:
        if number in self.freq:
            old_freq = self.freq[number]
            self.count[old_freq] -= 1
            if self.count[old_freq] == 0:
                del self.count[old_freq]
            new_freq = old_freq + 1
            self.freq[number] = new_freq
            if new_freq in self.count:
                self.count[new_freq] += 1
            else:
                self.count[new_freq] = 1
        else:
            self.freq[number] = 1
            if 1 in self.count:
                self.count[1] += 1
            else:
                self.count[1] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] > 0:
            old_freq = self.freq[number]
            self.count[old_freq] -= 1
            if self.count[old_freq] == 0:
                del self.count[old_freq]
            new_freq = old_freq - 1
            if new_freq > 0:
                self.freq[number] = new_freq
                if new_freq in self.count:
                    self.count[new_freq] += 1
                else:
                    self.count[new_freq] = 1
            else:
                del self.freq[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.count and self.count[frequency] > 0