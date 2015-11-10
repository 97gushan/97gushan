class Crop:
    """---"""
    
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount
        
    
    def __str__(self):
        """ this method returns a string that contains all the
        class arguments"""
        return self._name + ";" + str(self._amount)
        
        
        
crops = []

crops.append(Crop("Kalle", 10))
crops.append(Crop("Pelle", 15))


#for crop in crops:
    #print(crop)
    

# w - skriver till filen
# r - läser från filen
# a - skriv till slutet av filen
# t - textfil
# b - binärfil    
    
def write_to_file(inputs):
    """ this method writes to the file"""
    file = open("./testar.csv", 'w')
    
    for item in inputs:
        file.write(item.__str__() + "\n")
    
    file.close()
    
def read_from_file(output):
    """ this method reads from the file"""
    file = open("./testar.csv", "r")
    
    
    for line in file:
        # tar bort radavslut och mellanslag
        line.strip()
        
        item = line.split(";")
        print(item)
        output.append(Crop(item[0], int(item[1])))
        
    file.close()
    
write_to_file(crops)
corpse = []
read_from_file(corpse)

for crop in corpse:
    print(crop)
    
    
    
    
    
    
    