from src.sqlite_connect import sqlite_memory, sqlite_file
import pytest


def test_sqlite_memory():
    expected = 3
    ret = sqlite_memory()
    print('Version: "' + ret["db_ver"] + '"')
    print("sqlite3 memory db test")
    if "e_msg" not in ret:
        assert ret["fetch"] == expected
    else:
        print(f"e_msg: {ret["e_msg"]}")
        pytest.fail("e_msg unexpectedly found in ret dict")


def test_sqlite_file():
    exp_1 = [("a", 4, 9), ("b", 5, 12), ("c", 3, 16), ("d", 8, 12), ("e", 1, 9)]
    exp_2 = [("a", 4, 4), ("b", 5, 9), ("c", 3, 12), ("d", 8, 20), ("e", 1, 21)]
    ret = sqlite_file()
    print('Version: "' + ret["db_ver"] + '"')
    print("sqlite3 file-based db test")

    if "e_msg" not in ret:
        assert ret["fetch_1"] == exp_1
        assert ret["fetch_2"] == exp_2
    else:
        print(f"e_msg: {ret["e_msg"]}")
        pytest.fail("e_msg unexpectedly found in ret dict")
