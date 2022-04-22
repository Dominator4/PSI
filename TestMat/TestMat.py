
import Zadanie_tdd as z

def testMin():
    assert z.mat().min(2, 1) == 1

def testMax():
    assert z.mat().max(2, 1) == 2

def testIsPositive():
    assert z.mat().ispositive(-1) == False
