"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import PubSub

if __name__ == "__main__":
    ps = PubSub()
    log = []
    ps.subscribe("orders.created", lambda m: log.append(("exact", m)))
    ps.subscribe("orders.*", lambda m: log.append(("wild", m)))
    n = ps.publish("orders.created", "order-1")
    print("handlers invoked:", n)
    print("log:", log)
    print("publish to empty topic:", ps.publish("nothing", "x"))
