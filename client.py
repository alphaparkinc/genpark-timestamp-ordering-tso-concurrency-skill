class TimestampOrderingController:
    """Timestamp Ordering (TSO) protocol with Thomas Write Rule."""
    def __init__(self):
        self.r_ts = {}
        self.w_ts = {}

    def execute_read(self, tx_ts: int, item: str) -> dict:
        if tx_ts < self.w_ts.get(item, 0):
            return {"action": "ABORT", "reason": "Read older than last write"}
        self.r_ts[item] = max(self.r_ts.get(item, 0), tx_ts)
        return {"action": "ALLOW", "item": item, "r_ts": self.r_ts[item]}

    def execute_write(self, tx_ts: int, item: str) -> dict:
        if tx_ts < self.r_ts.get(item, 0):
            return {"action": "ABORT", "reason": "Write older than last read"}
        if tx_ts < self.w_ts.get(item, 0):
            # Thomas Write Rule: Obsolete write ignored without aborting
            return {"action": "IGNORE_OBSOLETE", "item": item}
        self.w_ts[item] = tx_ts
        return {"action": "ALLOW", "item": item, "w_ts": self.w_ts[item]}
