
def buchstbe_aendern(string = "banana", buchstabe = "a"):
    
    vokal = "aeiou"
    
    def buchstabe_ersetzen(x, y, z):
        
        x_list = list(x.lower())
        
        for i in range(len(x_list)):
            
            if x_list[i] == y:
                
                x_list[i] = z
                
        return "".join(x_list)
    
    for v in vokal:
        print(buchstabe_ersetzen(string, buchstabe, v), end = " ")

buchstbe_aendern(string = "banana", buchstabe = "a")
