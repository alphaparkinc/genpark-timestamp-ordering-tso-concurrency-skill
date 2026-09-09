import sys
import json
from client import TimestampOrderingController

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    tso = TimestampOrderingController()
    if method == "read":
        return tso.execute_read(params.get("ts", 1), params.get("item", "x"))
    elif method == "write":
        return tso.execute_write(params.get("ts", 1), params.get("item", "x"))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
