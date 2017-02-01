#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, do_collatz

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_3(self):
        s = "999999 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999999)
        self.assertEqual(j, 0)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6(self):
        v = collatz_eval(500, 1)
        self.assertEqual(v, 144)
    
    def test_eval_7(self):
        v = collatz_eval(1, 5000)
        self.assertEqual(v, 238)

    def test_eval_8(self):
        self.assertRaises(AssertionError, collatz_eval, -1, -5)
        # This should fail

    def test_eval_9(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_10(self):
        v = collatz_eval(10971, 11999)
        self.assertEqual(v, 268) 

    # ----
    # do_collatz
    # ----

    def test_do_1(self):
        v = do_collatz(1)
        self.assertEqual(v, 1)

    def test_do_2(self):
        v = do_collatz(55405)
        self.assertEqual(v, 79)

    def test_do_3(self):
        v = do_collatz(999999)
        self.assertEqual(v, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 8, 2, 500)
        self.assertEqual(w.getvalue(), "8 2 500\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 999999, 0, 1)
        self.assertEqual(w.getvalue(), "999999 0 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("900 1000\n1 1\n500 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n1 1 1\n500 1 144\n")

    def test_solve_3(self):
        r = StringIO("584 585\n586 587\n588 589\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "584 585 119\n586 587 119\n588 589 119\n")

    def test_solve_4(self):
        r = StringIO("        \n")
        w = StringIO()
        collatz_solve(r, w)

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1

% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK

% coverage-3.5 report -m                   >> TestCollatz.out

% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
