def open_file():

 nameHandle = open("QA_Pairs.txt", "r")

 lines = nameHandle.readlines()
 
    
 nameHandle.close()

 return lines

def count_pairs(my_list):
    
 new_string = str(my_list)
 
 counting = new_string.count('"answer":')
 
 return counting 
 
 
 
 
my_list = (open_file()) 
   
new_strinngs = count_pairs(my_list)

print(new_strinngs)



def unique_pairs(my_list):
    
    for x in range(len(my_list)):
        
        if my_list[x][0] == my_list[x+1][0]: #(q1,a1) == (q1,a1)
            
         text = my_list[x+1][0]
         with open("overlapping.txt", "w") as nameHandle:
          nameHandle.write(text)
         
         
         
        
    






"""
class myTests(unittest.TestCase):

 def test1(self):
  self.assertAlmostEqual(count_pairs(1))
  def test2(self):
      self.assertAlmostEqual(count_pairs(5))

if __name__ == '__main__':
    unittest.main(exit=True)
"""
