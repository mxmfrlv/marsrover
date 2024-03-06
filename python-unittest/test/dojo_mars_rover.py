import unittest

from wordcount.marsrover import MarsRover

class DojoMarsRover(unittest.TestCase):

    def test_shouldReturnErrorIfNotValid(self):
        marsRover = MarsRover()
        self.assertEqual(marsRover.command("X"), "Error")
        
    def test_getInitialCoordinates(self):
        marsRover = MarsRover()
        self.assertEqual(marsRover.getCoordinates(), [0, 0,"N"])
    
    def test_shouldTurnToTheLeft(self):
        marsRover = MarsRover()
        
        marsRover.command("L")
        
        self.assertEqual(marsRover.getCoordinates(), [0, 0,"W"])
        
    def test_shouldBeSouthAfterLL(self):
        marsRover = MarsRover()
        
        marsRover.command("LL")
        
        self.assertEqual(marsRover.getCoordinates(), [0, 0,"S"])
    
    def test_shouldTurnToTheRight(self):
        marsRover = MarsRover()
        
        marsRover.command("R")
        
        self.assertEqual(marsRover.getCoordinates(), [0, 0,"E"])

    def test_shouldBeOn2_2AfterMMRMM(self):
        marsRover = MarsRover()
        
        marsRover.command("MMRMM")
        
        self.assertEqual(marsRover.getCoordinates()[:2], [2, 2])

    def test_earthIsRound(self):
        earth_size=10
        shouldbedict={"LM":[earth_size-1,0],"LLM":[0,earth_size-1],"M"*earth_size:[0,0],"R"+"M"*earth_size:[0,0]}
        for command,result in shouldbedict.items():
            with self.subTest(command=command,shouldbe=result):
                #given:
                marsRover = MarsRover() 
                #when:
                marsRover.command(command)
                #then:
                self.assertEqual(marsRover.getCoordinates()[:2], result)


