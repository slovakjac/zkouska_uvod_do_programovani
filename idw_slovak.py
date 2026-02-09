#INTERPOLATION - METHOD IDW
#Jáchym Slovák, 2. B-FGG
#Choceň, 9. 2. 2026
#Introduction to programming (Úvod do programování) MZ370P19

from math import sqrt
from sys import exit

class Point:
    def __init__(self, x, y, z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
class IDW:
    def __init__(self, list_of_known_points):
        self.known_points=list_of_known_points

    def interpolation(self, x_new, y_new, k):
        all_distances=[]
        for b in self.known_points:
            s=sqrt((x_new-b.x)**2 + (y_new-b.y)**2)

            if s==0:
                return b.z
            all_distances.append([s,b])
        all_distances.sort(key=lambda x: x[0])
        closest_neighbours=all_distances[0:k]

        upper_sum=0
        lower_sum=0

        for line in closest_neighbours:
            distance=line[0]
            point=line[1]
            weight=1/distance
            upper_sum=upper_sum+(point.z*weight)
            lower_sum=lower_sum+weight
        return upper_sum/lower_sum
class File:
    def __init__(self,known_route,unknown_route,output_route):
        self.known_route=known_route
        self.unknown_route=unknown_route
        self.output_route=output_route

    def load_known_points(self):
        points=[]
        try:
            with open(self.known_route,"r") as f:
                line_number_first=0
                for line in f:
                    line_number_first+=1
                    line_clean=line.strip()
                    if not line_clean:
                        continue
                    if ";" in line_clean:
                        parts=line_clean.split(";")
                        if len(parts)==3:
                            try:
                                points.append(Point(float(parts[0]),float(parts[1]),float(parts[2])))
                            except ValueError:
                                print("Error. Input data has to be in the right format.")
                        else:
                            print(f"On line {line_number_first} are invalid coordinates. Line skipped.")
                    else:
                        print(f"Error. Line {line_number_first} lacks ';'. Line skipped.")
        except FileNotFoundError:
            print("Error. File not found.")
        except Exception as e:
            print(f"Unexpected error {e}")
        return points
    def calculation_and_result(self,tool_idw,k):
        try:
            with open(self.output_route, "w") as o:
                with open(self.unknown_route,"r") as v:
                    line_number=0
                    for line in v:
                        line_number+=1
                        line_clean=line.strip()
                        if not line_clean:
                            continue
                        if ";" in line_clean:
                            parts=line_clean.split(";")
                            if len(parts)==2:
                                try:
                                    x_unknown=float(parts[0])
                                    y_unknown=float(parts[1])
                                    result_z=tool_idw.interpolation(x_unknown,y_unknown,k)
                                    o.write(f"{x_unknown}; {y_unknown}; {result_z:.4f}\n")
                                except ValueError:
                                    print("Error. Input data has to be in the right format")
                            else:
                                print(f"Line {line_number} has invalid coordinates. Line skipped.")
                        else:
                            print(f"Error. Line {line_number} lacks ';'. Line skipped.")
            print("Finished. Results saved in file 'vystup_idw_slovak.txt'.")
        except FileNotFoundError:
            print("Error! File not found.")
        except Exception as e:
            print(f"Unexpected error {e}.")

class App:
    def __init__(self, file_known,file_unknown,output_file):
        self.admin=File(file_known,file_unknown,output_file)
    def get_k(self,max_value):
        while True:
            try: 
                k=int(input(f"Input number of closest neighbours (max {max_value}): "))
                if 0<k<=max_value:
                    return k
                else:
                    print(f"Invalid range. Input number between 1 and {max_value}.")
            except ValueError:
                print("Error, input integer.")
    def launch(self):
        known_points=self.admin.load_known_points()
        if not known_points:
            print("No data found.")
            exit()
        k=self.get_k(len(known_points))
        idw_tool=IDW(known_points)
        self.admin.calculation_and_result(idw_tool,k)

app=App("zname_body_idw.txt", "nezname_body.txt", "vystup_idw_slovak.txt")
app.launch()
