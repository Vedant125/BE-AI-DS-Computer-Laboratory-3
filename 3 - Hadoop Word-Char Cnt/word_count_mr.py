'''Design a distributed application using MapReduce under Hadoop 
for: a) Character counting in a given text file. b Counting no. of 
occurrences of every word in a given text file. '''
from mrjob.job import MRJob
import re

WORD_REGEXP = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_REGEXP.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
