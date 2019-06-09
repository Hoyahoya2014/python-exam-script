#! /bin/bash/python

_NUM1 = int(input("ENTER NUMBER 1 :"))
_NUM2 = int(input("ENTER NUMBER 2 :"))
_NUM3 = int(input("ENTER NUMBER 3 :"))


def _COMPARE_NUMBER(_NUMBER1,_NUMBER2,_NUMBER3) : #function compare
    _MIN_VAL =""
    _MAX_VAL =""
    _LIST_INPUT = []
  

    if _NUMBER1 > _NUMBER2 and _NUMBER1 > _NUMBER3 :
        _MAX_VAL = "NUMBER INPUT 1 IS MAX"
        _MAX_CAL = _NUMBER1
    elif _NUMBER2 > _NUMBER1 and _NUMBER2 > _NUMBER3 :
        _MAX_VAL = "NUMBER INPUT 2 IS MAX"
        _MAX_CAL = _NUMBER2
    elif _NUMBER3 > _NUMBER1 and _NUMBER3 > _NUMBER2 :
        _MAX_VAL = "NUMBER_INPUT 3 IS MAX"
        _MAX_CAL = _NUMBER3
    else :
        _MAX_VAL ="CANNOT SPECIFY MAX VAL"
        _MAX_CAL = _NUMBER1


    if _NUMBER1 < _NUMBER2 and _NUMBER1 < _NUMBER3 :
        _MIN_VAL = "NUMBER INPUT 1 IS MIN"
        _MIN_CAL = _NUMBER1
    elif _NUMBER2 < _NUMBER1 and _NUMBER2 < _NUMBER3 :
        _MIN_VAL = "NUMBER INPUT 2 IS MIN"
        _MIN_CAL = _NUMBER2
    elif _NUMBER3 < _NUMBER1 and _NUMBER3 < _NUMBER2 :
        _MIN_VAL = "NUMBER INPUT 3 IS MIN"
        _MIN_CAL = _NUMBER3
    else :
        _MIN_VAL = "CANNOT SPECIFY MIN VAL"
        _MIN_CAL = _NUMBER1

    
    _LIST_INPUT = [_MIN_CAL,_MAX_CAL]

    _SUM_NUMBER = "SUM VALUE MIN+MAX : {0}".format(_CAL_NUMBER(_LIST_INPUT))
    return [_MAX_VAL,_MIN_VAL,_SUM_NUMBER]


def _CAL_NUMBER(_ARR_VAR) : #func calculate 
    _TOTAL=0
    if len(_ARR_VAR) > 0 :
        for i in range(0,len(_ARR_VAR)) :
            _TOTAL =_TOTAL+int(_ARR_VAR[i])
    return _TOTAL



_ARR_DATA = _COMPARE_NUMBER(_NUM1,_NUM2,_NUM3)

print("OUT PUT : \n {0} \n {1} \n {2}".format(_ARR_DATA[0],_ARR_DATA[1],_ARR_DATA[2]))    
