# LLM Reader Archaeology — find the missing step before the reader does

An LLM (and a human new to derivatives) often fails at the same point: a sentence contains a technically correct word or formula, but the object that gives the word meaning is still invisible. Treat that as a manuscript bug.

## The four questions for every technical sentence

Before keeping a sentence containing a formula, symbol, or finance label, ask:

1. **What object is this about?** Show the contract, cash amount, state, date, or price first.
2. **What changed?** Put the before-and-after or low-and-high cases in a table.
3. **What does each new symbol stand for?** Translate it in the sentence immediately before the formula.
4. **What kind of conclusion is this?** Say whether it is a contract fact, arithmetic result, model assumption, or strategy judgment.

If any answer is missing, do not add another sentence of jargon. Add the missing row, definition, or date first.

## The formula order

`visible example → table of cases → arithmetic in ordinary words → named shape or concept → compact formula → limitation`

The compact formula is a bookmark for a pattern already seen. It is never the first appearance of the pattern.

## Repairs made from reader feedback

| Chapter | Reader-visible jump | Repair |
|---:|---|---|
| 003 | “Reality resists” introduced broker mechanics before the two-booth logic was stable. | Replaced with four plain checks on the same two booths. |
| 004 | A $110 forward quote, low-quote reverse trade, and dividend yield appeared without full cash paths. | Added dated high/low forward tables; replaced yield shorthand with a known $4 dividend table. |
| 006 | “Convex kink” and expectation notation appeared before the payoff table did its work. | Added still-versus-moving payoff table; postponed the name convex and removed premature expectation notation. |
| 008 | `Delta` arrived as a formula label. | Added an up/down difference table and found the half-share before naming the hedge ratio. |
| 013 | Jensen’s inequality appeared before its table and symbol translation. | Added the still/wide table; defined `E[...]`, `f(X)`, and convex before showing the compact inequality. |

## Audit flags to search for

The following words are not forbidden. They are alarms that demand an immediately preceding explanation:

`therefore`, `it follows`, `convex`, `expected`, `fair`, `risk-neutral`, `replication`, `drift`, `measure`, `martingale`, `PDE`, `calibration`, `arbitrage-free`, `cheap`, `expensive`.

For each alarm, ask: *where is the table or small example that made this sentence inevitable?*

## The two acceptable outcomes

After the audit, a chapter may say either:

- **“Here is the result.”** The table and arithmetic make it checkable.
- **“We cannot yet say.”** A required definition, market fact, or model assumption is still missing.

The second answer is a success. It keeps a teaching book from turning an unexplained formula into a fake explanation.
