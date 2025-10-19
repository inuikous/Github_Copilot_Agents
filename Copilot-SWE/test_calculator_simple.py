from calculator import evaluate_expression, CalcError

def run_tests():
    cases = [
        ("1+2*3", 7),
        ("(4-7)/2", -1.5),
        ("-3+5", 2),
        ("10/2", 5),
    ]
    ok = True
    for expr, expected in cases:
        res = evaluate_expression(expr)
        print(f"{expr} -> {res} (expected: {expected})", "OK" if res == expected else "FAIL")
        if res != expected:
            ok = False
    # test invalid expression
    try:
        evaluate_expression("__import__('os').system('echo hi')")
        print("security FAIL")
        ok = False
    except CalcError:
        print("security OK")

    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(run_tests())
