class A:
    def __init__(self):
        print("in A  ")
    def feature1(self):
        print("feature 1-a working")

    def feature2(self):
        print("feature 2 working")

class B:
    def __init__(self):
        print("in b")
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in c")


a1=C()
a1.feature1()





