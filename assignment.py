class Time: 
   def __init__(self,hour=0,minute=0):
       self.hour =hour
       self.minute =minute
       self.normalize_time()

   def normalize_time(slef):
       self.hour = (self.hour + self.minute //60) % 24
       self.minute =self. minute %60

   def tick(self):
       self. minute +=1
       self. normalize_time()

   def __sub__(self, other)
       total_minutes_self =self.hour * 60 +self.minute
       total_minutes_other = other. hour*60+ other.minute
       diff_minutes =abs(total_minutes_self -total_minutes_other)
       hour = diff_minutes //60
       minutes =diff_minutes %60
       return f"{hours} hour(s) and {minutes} minutes(s)"

   def __str__(self):

       return f"{self.hour:02d}:{self.minutes:02d}"

   def getTime(self)
       return (self.hour, self. minute)

   def setTime(self, hour, minute):
       self.hour =hour
       self.minute =minute
       self.normalize_time()

   def __It__(self, other)
       return (self.hour, self.minute) < (other.hour,other.minute)

   def __len__(self):
       return self.hour *60+ self.minute
