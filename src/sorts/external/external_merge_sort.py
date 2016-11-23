import random
class QSort:
    def quicksort(self, arr):
        self.split(arr, 0 , len(arr) - 1)
    def split(self, arr, low, high):
        if high - low > 0:
            pivot = self.partition(arr, low, high)
            self.split(arr, low, pivot - 1)
            self.split(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        self.swap(arr, low, random.randint(low, high))
        pivotValue = arr[low]
        left = low + 1
        right = high
        while True:
            while left <= right and arr[left] < pivotValue:
                left += 1
            while left <= right and arr[right] >= pivotValue:
                right -= 1
            if left > right:
                break
            self.swap(arr, left, right)
        self.swap(arr, right, low)
        return right

    def swap(self, arr, low, high):
        arr[low], arr[high] = arr[high], arr[low]
   

file_name_template = "unsorted_chunk_{0}.txt"
filename_sorted = "sorted_chunk_{0}_level_{1}.txt"

def break_up_files(unsortedFile):
    with open(unsortedFile, 'r') as a_file:
        counter = 0
        maxLines = 500
        lines = []
        numberFile = 0

        for line in a_file:
            lines.append(line)
            counter += 1
            if maxLines == counter:
                with open(file_name_template.format(numberFile), 'w') as unsorted_chunk:
                    for value in lines:
                        unsorted_chunk.write(value)
                lines = []
                counter = 0
                numberFile += 1
    return numberFile

def sortChunk(fileNumber):
    unsortedFileChunk = file_name_template.format(fileNumber)
    with open(unsortedFileChunk, 'r') as i:
        lines = []
        for line in i:
            lines.append(int(line))
    qsort = QSort()
    qsort.quicksort(lines)
    sortedChunkFileName = filename_sorted.format(fileNumber, 0)
    with open(sortedChunkFileName, 'w') as f:
        for line in lines:
            f.write(str(line) + "\n")
                    
def mergeChunks(numberOfFiles, level):
    print(numberOfFiles, level)
    i = 0
    j = numberOfFiles - 1
    while i < j:
        a = filename_sorted.format(i, level - 1)
        b = filename_sorted.format(j, level - 1)
        mergedFile = filename_sorted.format(i, level)
        with open(mergedFile, 'w') as mergedChunk:
            with open(a, 'r') as aFile:
                with open(b, 'r') as bFile:
                    aval = aFile.readline()
                    bval = bFile.readline()
                    
                    while aval and bval:
                        aval = int(aval)
                        bval = int(bval)
                        if aval <= bval:
                            mergedChunk.write(str(aval)+"\n")
                            
                            aval = aFile.readline()
                            if aval == '':
                                break
                            aval = int(aval)
                        else:
                            mergedChunk.write(str(bval)+"\n")
                            bval = bFile.readline()
                            if bval == '':
                                break
                            bval=int(bval)
                               
                    while aval:
                        mergedChunk.write(str(aval)+"\n")
                        aval = aFile.readline()
                        if not aval:
                            break
                        aval = int(aval)
                    while bval:
                        mergedChunk.write(str(bval)+"\n")
                        bval = bFile.readline()
                        if not bval:
                            break
                        bval = int(bval)
        i += 1
        j -= 1
    if i % 2:
        return i
    return i - 1


def external_merge_sort(unsortedFile):
    numberOfFiles = break_up_files(unsortedFile)
    print(numberOfFiles, " Chunks")
    for fileNumber in range(numberOfFiles):
        sortChunk(fileNumber)

    level = 0
    while int(numberOfFiles) > 1:
        print("NumberOfFiles:{0}".format(numberOfFiles))

        level += 1
        numberOfFiles = mergeChunks(numberOfFiles, level)

external_merge_sort('unsorted_ids.txt')

