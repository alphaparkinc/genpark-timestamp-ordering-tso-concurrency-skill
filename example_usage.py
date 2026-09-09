from client import TimestampOrderingController

def main():
    print("=== Timestamp Ordering (TSO) Controller ===")
    tso = TimestampOrderingController()

    res_w10 = tso.execute_write(10, "account")
    assert res_w10["action"] == "ALLOW"

    res_r12 = tso.execute_read(12, "account")
    assert res_r12["action"] == "ALLOW"

    # Write from older Tx 8 is rejected because read at 12 already occurred
    res_w8 = tso.execute_write(8, "account")
    print("Older Write Attempt Result:", res_w8)
    assert res_w8["action"] == "ABORT"

    print("TSO Controller verified successfully!")

if __name__ == "__main__":
    main()
