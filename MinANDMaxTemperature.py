from mrjob.job import mrjob
class MinANDMaxTemperature(mrjob):
    def mapper(self,key,line):
        line=line.split(',')
        loc,temp=line[0],line[3]
        fahrenheit=(int(temp)*1.8)+32
        yield loc,fahrenheit
    def reducer(self,loc,fahrenheit):
        min_temp=next(fahrenheit)
        max_temp=min_temp
        for item in fahrenheit:
            min_temp=min(item,min_temp)
            max_temp=max(item,max_temp)
        yield loc,(min_temp,max_temp)
        
if __name__ == '__main__':
    MinANDMaxTemperature.run()
    
    
    