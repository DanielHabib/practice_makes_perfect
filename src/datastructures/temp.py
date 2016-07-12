class TempTracker:
    def __init__(self):
	self.total = 0
	self.mode = 0
	self.max = 0	
	self.min = 100000
	self.count = 0
	self.occurence_dict = {}
	self.mode_count = 0

    def insert(self, temp):
        self.total += temp
	self.count += 1
	self.max = max(temp, self.max)
	self.min = min(temp, self.min)

	if self.occurence_dict.get(temp, False):
		self.occurence_dict[temp] += 1
	
	if self.occurence_dict[temp] > self.mode_count:
	    self.mode_count = self.occurence_dict[temp]
	    self.mode = temp

    def get_max(self):
        # Constant Time possible if we have a sorted array
	if len(self.sorted) > 0:
            return self.sorted_temps[-1]
    
    def get_min(self):
        # Constant Time possible if we have a sorted array
	if len(self.sorted) > 0:
	    return self.sorted_temps[0]
	
        return self.sorted_temps[0]
    
    def get_mean(self):
        # Constant Time possible if we maintain a total count
        # Return a float
        if len(self.sorted) > 0:
	    return self.total / len(self.sorted)

    
    def get_mode(self):
        # Constant time possible if we leverage a priority queue or we recalculate on our sorted
        # Array after each new element is added. We will keep count using a dictionary
        return self.mode

    
# run your function through some test cases here
# remember: debugging is half the battle!
temptracker = TempTracker()

print temptracker.insert()
print temptracker.get_max()
print temptracker.get_min()
print temptracker.get_mean()
print temptracker.get_mode()

