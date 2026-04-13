from mrjob.job import MRJob
from mrjob.step import MRStep

class WeatherAnalysisMR(MRJob):

    def mapper(self, _, line):
        if not line.startswith('Year'):
            parts = line.split(',')
            year = parts[0]

            try:
                temp = float(parts[1])  # Tmax column
                yield year, temp
            except:
                pass

    def reducer_avg(self, year, temps):
        temps = list(temps)
        avg_temp = sum(temps) / len(temps)
        yield "avg", (year, avg_temp)

    def reducer_extreme(self, key, values):
        data = list(values)

        hottest = max(data, key=lambda x: x[1])
        coolest = min(data, key=lambda x: x[1])

        yield "Hottest Year", hottest
        yield "Coolest Year", coolest

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_avg),
            MRStep(reducer=self.reducer_extreme)
        ]

if __name__ == '__main__':
    WeatherAnalysisMR.run()