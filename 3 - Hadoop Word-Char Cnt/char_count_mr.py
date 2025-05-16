'''Design a distributed application using MapReduce under Hadoop 
for: a) Character counting in a given text file. b Counting no. of 
occurrences of every word in a given text file. '''
#CHAR COUNT
from mrjob.job import MRJob

class MRCharCount(MRJob):

    def mapper(self, _, line):
        for char in line.strip():
            yield char, 1

    def reducer(self, char, counts):
        yield char, sum(counts)

if __name__ == '__main__':
    MRCharCount.run()


# command to run the script from terminal or command line
# python char_count_mr.py input.txt > char_output.txt
# python file_name.py input.txt > output.txt
# Check other ways to run the code (eg in hadoop , etc)