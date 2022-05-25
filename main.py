class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self , name: str,  age: int, tracks: list, score: float):
        self.name=name
        self.age=age
        self.tracks=tracks

    def change_name(self, name: str):
        self.name =name
        return self.name
    
    def change_age(self, age: int):
        self.age = age
        return self.age

    def add_track(self, track: str):
        self.tracks.append(track)
        return self.tracks

    def get_score(self, score: float):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Tesla = Student(name="Tesla", age=99, tracks=["KSKS","JK"],score=19.90)

#Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()





