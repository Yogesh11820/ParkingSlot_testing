from project_code import ParkingLot
import Vehicle

P = ParkingLot()

def test_newlot3():
        assert P.create_parking_lot(3) == 3

def test_parkcar1():
        assert P.park(101,'Red') == 1

def test_parkcar2():
        assert P.park(102,'Blue') == 2

def test_parkcar3():
        assert P.park(103,'White') == 3

def test_parkcar4():
        assert P.park(104,'Black') == -1

def test_leave1():
        assert P.leave_slot(1) == True

def test_leave2():
        assert P.leave_slot(1) == False

def test_status():
        assert P.check_status() == None

def test_regno_color1():
       assert P.get_regno_from_color('White') == [103]

def test_regno_color2():
       assert P.get_regno_from_color('Black') == []

def test_regno_color3():
       assert P.get_regno_from_color('Blue') == [102]

def test_slotno_reg1():
        assert P.get_slotno_from_regno(101) == -1

def test_slotno_reg2():
           assert P.get_slotno_from_regno(102) == 2

def test_slotno_reg3():
           assert P.get_slotno_from_regno(103) == 3

def test_slotno_color1():
        assert P.get_slotno_from_color('Blue') == ['2']

def test_slotno_color2():
        assert P.get_slotno_from_color('White') == ['3']

def test_slotno_color3():
        assert P.get_slotno_from_color('Yellow') == []
      



       
         
