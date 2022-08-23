class Pembalap:
  pemCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Pembalap.pemCount += 1
   
  def displayCount(self):
    print ("Total Pembalap %d" % Pembalap.pemCount)

  def displayPembalap(self):
    print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Pembalap class"
pem1 = Pembalap("Verstappen", 2000)
#This would create second object of Pembalap class"
pem2 = Pembalap("Leclerc", 5000)
pem1.displayPembalap()
pem2.displayPembalap()
print ("Total Pembalap %d" % Pembalap.pemCount)