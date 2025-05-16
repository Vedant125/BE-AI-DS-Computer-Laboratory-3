from mrjob.job import MRJob
from mrjob.step import MRStep

class Min_temp(MRJob):

    def mapper(self, _, line):
        year, temp = line.strip().split(',')
        yield year, float(temp)

    def reducer_find_min_temp(self, year, temps):
        min_temp = min(temps)
        yield None, (year, min_temp)

    def reducer_find_year_with_min_temp(self, _, year_temp_pairs):
        year_with_min_temp = min(year_temp_pairs, key=lambda x: x[1])
        yield year_with_min_temp

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_find_min_temp),
            MRStep(reducer=self.reducer_find_year_with_min_temp)
        ]

if __name__ == "__main__":
    Min_temp.run()
