
class matriculation:
    # grade = 10
    # result = '88%'
    def __init__(self,grade_10, result_10):
        self.grade_10 = grade_10
        self.result_10 = result_10

    def detail(self):
        return dict(self.grade_10, self.result_10)

class senior_secondary(matriculation):
    # grade_12 = 12
    # result_12 = '98%'

    def __init__(self, grade_12, result_12, grade_10, result_10):
        super().__init__(grade_10, result_10)
        self.grade_12 = grade_12
        self.result_12 = result_12

    def detail(self):
        return (super().detail()).update( {self.grade_12: self.result_12})

class graduation(senior_secondary):
    # grade_graduation = "b.tech"
    # result_graduation = '75'

    def __init__(self, grade_graduation, result_graduation, grade_12, result_12, grade_10, result_10):
        super().__init__(grade_12, result_12, grade_10, result_10)
        self.grade_graduation = grade_graduation
        self.result_graduation = result_graduation

    def detail(self):
        return (super().detail()).update({self.grade_graduation: self.result_graduation})
    


res = graduation("b.tech", 78, "12", 87, "10", 88)

print(res.detail())

