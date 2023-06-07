from mrjob.job import MRJob
class WordFrequency(MRJob):
    def mapper(self , _ , line):
        Words=line.split()
        for word in Words:
            yield word.lower(),1
    def reducer(self,key,values):
        yield key,sum(values)
        
if __name__ == '__main__':
   WordFrequency.run()        
         