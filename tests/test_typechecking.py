from typechecking import *

def test():
    te = typecheck(BinOp("+", Int(2), Int(3)))
    assert te == Int
    te = typecheck(BinOp("<", Int(2), Int(3)))
    assert te == Bool
    try:
        typecheck(BinOp("+", BinOp("*", Int(2), Int(3)), BinOp("<", Int(2), Int(3))))
        print("No error detected")
        return -1
    except:
        print("Error detected")
        pass

    te1 = typecheck(BinOp(">", Int(4), Int(2)))
    assert te1 == Bool
    te2 = typecheck(BinOp("+", Int(4), Int(2)))
    assert te2 == Int
    te3 = typecheck(BinOp("-", Int(4), Int(2)))
    assert te3 == Int
    try:
        typecheck(If(BinOp(">", Int(4), Int(2)), BinOp("+", Int(4), Int(2)), BinOp("-", Int(4), Int(2))))
        print("No error detected")
        return -1
    except:
        print("Error detected")
        pass

    print("All testcases passed")
    return 0

if(__name__ == "__main__"):
    test()