#HASHING - SEPARATE CHAINING
#Jáchym Slovák, 2. B-FGG
#Choceň, 9. 2. 2026
#Introduction to programming (Úvod do programování) MZ370P19  

class Hashtable:
    def __init__(self,size=10):
        self.size=size
        self.bins=[]
        for i in range(self.size):
                self.bins.append([])
            
    def hash_function(self,key):
            first_symbol=key[0]
            ascii_code=ord(first_symbol)
            index=ascii_code%self.size
            return index
        
    def add(self,key,value):
            index_bin=self.hash_function(key)
            self.bins[index_bin].append([key,value])

class File:
    def __init__(self, input_route, output_route):
        self.input_route=input_route
        self.output_route=output_route
        
    def load_data(self, table): 
        try:
            with open(self.input_route,"r",encoding="utf-8") as f:
                line_number=0
                for line in f:
                    line_number+=1
                    line=line.strip()
                    if not line:
                        continue
                    if ";" in line:
                        parts= line.split(";")

                        if len(parts)==2:
                            key=parts[0].strip()
                            value=parts[1].strip()
                            table.add(key,value)
                            if len(parts)>2:
                                print(f"Attention! On line {line_number} multiple values were found. Only the key and the first value were considered.")

                        else:
                            print(f"Error, line {line_number} lacks value. Line skipped.")
                    else:
                        print(f"Error. Line {line_number} lacks ';'.")

        except FileNotFoundError:
            print(f"Error, file {self.input_route} was not found")
        except Exception as e:
            print(f"Unexpected error {e}.")

    def save_data(self, table):
        try:
            with open(self.output_route, "w", encoding="utf-8") as o:
                for i in range(table.size):
                    bin=table.bins[i]
                    bin_count=len(bin)

                    list=[]
                    for pair in bin:
                        list.append(f"({pair[0]}: {pair[1]})")
                    bin_exctract=",".join(list)
                    o.write(f"Bin {i}, (count: {bin_count}): {bin_exctract}\n")

            print(f"Finished. Output saved successfully in file {self.output_route}")
        except Exception as e:
             print(f"Unexpected error {e}.")

my_table=Hashtable()
files=File("vstup_separate_chaining.txt","vystup_sc_slovak.txt")
files.load_data(my_table)
files.save_data(my_table) 




        