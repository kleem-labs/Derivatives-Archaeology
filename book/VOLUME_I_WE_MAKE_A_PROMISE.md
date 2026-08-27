# Volume I — We Make a Promise

Mara grows wheat. Arun bakes bread. Neither knows March's wheat price. Mara is frightened of a low price. Arun is frightened of a high one. The whole book begins with that small, familiar problem: how can two people make tomorrow less frightening without pretending they know tomorrow?

## 000 — A promise about the future

Mara says, “In March, I will sell you wheat for $6 a bushel.” Arun says yes.

If March wheat costs $9, Arun has a good deal: he pays $6 for something worth $9. If it costs $4, he has a bad deal: he still pays $6. The promise helps Arun when prices rise and hurts him when prices fall. Mara feels exactly the opposite.

The promise does not create wheat. It moves a risk from one pair of shoulders to another.

That is a derivative in its simplest form: a written rule whose value changes because something else changes. Before asking what the promise costs today, we must write exactly what it pays in each possible future.

[Open the workshop for this chapter](../excavations/000-a-promise-about-the-future/README.md)

## 001 — A right is different from a promise

Arun notices a problem. The $6 promise protects him from expensive wheat, but it also stops him enjoying cheap wheat.

So he asks for a different agreement: “In March, let me buy at $6 if I want to.” If wheat costs $9, he uses the right. If wheat costs $4, he walks away and buys in the market.

The words “if I want to” matter. They turn a straight line into a bent shape. Below $6, the right gives Arun nothing. Above $6, it saves him the difference.

We write that saving as `max(market price - agreed price, 0)`. Read it aloud: choose the bigger of the saving and zero. The `max` is not clever mathematics. It is simply the freedom to say no.

[Open the workshop for this chapter](../excavations/001-payoffs-before-prices/README.md)

## 002 — A dollar has a date attached

Arun's new right may ask him for $105 next year. How much cash today will grow into exactly $105 then?

At 5% interest, it is a little less than $100: about $99.88. Put $99.88 in the bank today and it becomes $105 in a year.

This is called discounting. It is just walking money backward through time. Future cash is divided by the growth it would have earned on the way.

`today's cash = future cash ÷ growth`

Notice what this does **not** do. It does not guess whether wheat will be high or low. It only moves a known amount of cash from one date to another. That is enough to compare two promises that finish with the same cash in the same future.

[Open the workshop for this chapter](../excavations/002-time-value-of-money/README.md)

## 003 — Same future, same price

Imagine two shops. Each sells a ticket that pays $105 next year. One costs $100. The other costs $101.

Buy the cheap ticket. Sell the expensive one. You receive $1 today. Next year, the two $105 payments cancel each other. Nothing about weather, wheat, or the stock market can spoil the trade.

This is the heart of no-arbitrage: if two things always give the same result, they cannot keep different prices. Otherwise people buy the cheaper one and sell the dearer one until the gap closes.

Real markets have fees, delays, and limits, so the rule becomes less tidy there. But the idea remains powerful. To value a complicated promise, try to build a simple copy of it. If the copy always behaves the same way, both should cost the same.

[Open the workshop for this chapter](../excavations/003-no-arbitrage/README.md)

## 004 — Two ways to get one share

Suppose one share costs $100 today. You can borrow $100, buy it now, and keep it for a year. At 5% interest, the loan becomes $105.13.

Or you can agree today to receive one share in a year. If the two routes really end with the same share on the same day, the second route should cost $105.13 too. If it asks for $110, buy the share now and promise to deliver it later. If it asks for much less, the opposite trade may work if you can borrow the share.

The formula is only a short version of the story:

`future delivery price = today's share price × interest growth`

If owning the share pays a dividend, include that cash too. Do not memorize the formula. Draw both routes and list what each route gives and takes.

[Open the workshop for this chapter](../excavations/004-forward-price/README.md)

## 005 — The promise can ask for money early

A forward waits until the end. A futures contract settles its gain or loss every day.

If Arun buys a wheat future at $6 and it closes at $6.20 tonight, money appears in his account tonight. If it closes at $5.80 tomorrow, money leaves his account tomorrow. The final economic result may resemble a forward, but the journey does not.

This matters because a hedge can be sensible at the finish and impossible in the middle. Mara may own wheat that will eventually offset a futures loss, yet still lack cash for today's margin call.

The book has now made two kinds of promise: one that fixes a price for both people, and one that settles along the way. Arun still wants protection from expensive wheat without giving up cheap wheat. The next volume gives him that one-sided choice.

[Open the workshop for this chapter](../excavations/005-futures-marking-to-market/README.md)

## What to carry with you

- A derivative is a written rule about a changing thing.
- A payoff says what the rule gives in each future.
- Money must be moved between dates before it can be compared.
- Two routes that always end alike should not keep different prices.

The next question is beautiful because it is unfair in exactly one direction: can a person keep the good future and refuse the bad one?

[Next volume: We Build the Asymmetry](VOLUME_II_WE_BUILD_THE_ASYMMETRY.md)

