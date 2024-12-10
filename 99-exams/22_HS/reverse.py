class Airplane:
    def __init__(self, airplane_type, name):
        self.type = airplane_type
        self.name = name
        self.passengers = []

    def board(self, passengers):
        self.passengers = passengers

    def get_passengers(self, number=-1):
        if number == -1:
            return self.passengers
        else:
            return [a for a in self.passengers if a[1] == "business class" ]


    def parse_manifest(input_str):
        out = []
        for a in input_str.split(";"):
            elements = str(a).split(",")
            name = elements[0] + " " + elements[1]
            out.append(Passenger(name, int(elements[2])))
        return out

class Passenger:
    def __init__(self, name, flight_class):
        self.name = name
        if flight_class == 1:
            self.flight_class = "1st class"
        elif flight_class == 2:
            self.flight_class = "business class"
        elif flight_class == 3:
            self.flight_class = "economy class"

    def __repr__(self):
        out = self.name + ", " + self.flight_class
        return out

    def __getitem__(self, item):
        if item == 0:
            return self.name
        elif item == 1:
            return self.flight_class



if __name__ == '__main__':
    passengers = Airplane.parse_manifest(("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
    a = Airplane("A388", "G-XLEK")
    a.board(passengers)
    print(a.get_passengers())
    p = a.get_passengers(2)
    #print(p)
    print(type(p[1]))
    print(p[1])