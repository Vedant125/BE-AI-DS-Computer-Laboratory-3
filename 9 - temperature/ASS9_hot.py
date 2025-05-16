# Design and develop a distributed application to find the coolest/hottest year from the available weather data. 
# Use weather data from the Internet and process it using MapReduce.

from mrjob.job import MRJob
from mrjob.step import MRStep

class Max_temp(MRJob):

    def mapper(self,_, line):
        year, temp = line.split(',')
        yield year, float(temp)

    def reducer_find_max_temp(self, year, temp):
        max_temp = max(temp)
        yield None, (year, max_temp)

    def reducer_find_year_with_max_temp(self,_, year_temp_pairs):
        year_with_max_temp = max(year_temp_pairs, key=lambda x: x[1])
        yield year_with_max_temp

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_find_max_temp),
            MRStep(reducer=self.reducer_find_year_with_max_temp)
        ]

if __name__ == "__main__":
    Max_temp.run()
