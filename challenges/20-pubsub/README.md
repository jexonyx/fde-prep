# 20 — pubsub

**Tier 3 · ~35 min.**

## Concepts drilled
A topic → handlers registry, calling back into caller-supplied functions, **fault isolation**
(one bad handler must not break the others), and **wildcard matching** by topic segments.

## Problem statement
Build a `PubSub`:
- `subscribe(topic, handler)` — register `handler` (a callable taking one `msg` argument) for
  `topic`.
- `publish(topic, msg)` — call every handler subscribed to `topic` with `msg`. Return the
  number of handlers invoked. Publishing to a topic with no subscribers is fine (returns 0).
- `unsubscribe(topic, handler)` — remove that handler from that topic. Return `True` if
  something was removed, `False` otherwise.

**Fault isolation:** if a handler raises, it must not prevent the other handlers from
running, and must not propagate out of `publish`.

## Worked example
```
ps = PubSub()
received = []
ps.subscribe("orders", received.append)
ps.publish("orders", "order-1")    # received == ["order-1"], returns 1
ps.publish("empty", "x")           # returns 0, no error
ps.unsubscribe("orders", received.append)
ps.publish("orders", "order-2")    # received unchanged, returns 0
```

## Constraints / assumptions
- Handlers are called in subscription order. The same handler may be subscribed once per
  topic (you can keep it simple: one registration per (topic, handler)).
- Topics are dot-separated strings.

## Follow-up extensions  → `TestStretch`
1. **Wildcard topics:** a subscription topic may contain `*`, which matches exactly **one**
   segment. `subscribe("orders.*", h)` fires on `publish("orders.created", ...)` and
   `publish("orders.shipped", ...)`, but not `publish("orders.created.eu", ...)` (segment
   count must match). Both exact and wildcard subscribers of a published topic fire.

## Edge cases to consider
- Publishing to no subscribers.
- A handler that raises (others still run; `publish` doesn't raise).
- `unsubscribe` of something never subscribed.

## Complexity target
`publish` is O(S · matching cost) over S subscriptions in the simple design. Be ready to note
that exact-topic dispatch can be O(1) with a dict, and wildcards are the part that forces a
scan (and how a trie of segments would speed it up).

## Narration prompts
- "Subscriptions live in a dict from topic-pattern to a list of handlers; publish finds the
  matching patterns and calls their handlers in order."
- Stress the try/except around each handler: "fault isolation — I swallow a handler's
  exception so siblings still run."
- For wildcards: "I match segment-by-segment; `*` matches any single segment, lengths must
  agree."
