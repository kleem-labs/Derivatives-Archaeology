# 032 — Commodities and Convenience Yield

Physical ownership can keep a refinery running, meet an emergency order, or avoid a stockout. This non-cash service is convenience yield `y`. An idealized commodity relation is `F_0=S_0e^((r+u-y)T)`.

Convenience yield is often inferred as the residual making observed spot, forward, rates, and storage consistent. It is not directly tradable and can rise when inventories are scarce. Short-selling physical goods may be impossible, so reverse cash-and-carry bounds can be weak.

Commodity forward curves therefore encode financing, storage, scarcity, seasonality, and constraints—not a simple forecast.

## The refinery cannot eat a futures contract

An oil refinery with nearly empty tanks faces a shutdown if a shipment is delayed. A futures position may gain when oil rises, but it cannot keep the machinery running today. Physical inventory provides a service beyond resale value: availability.

Convenience yield names that service in carry equations. When inventories are abundant, the service may be small. When scarcity threatens operations, it can be large enough that spot trades above deferred futures, a condition called backwardation under common usage. When financing and storage dominate, deferred prices may exceed spot, producing contango.

These curve shapes are not simple bullish or bearish forecasts. A rising curve can coexist with an expected falling spot if risk premia and carry differ; a backwardated curve can reflect acute current scarcity.

## Infer with humility

Rearrange `F_0=S_0e^((r+u-y)T)` to infer `y` after observing spot, forward, funding, and storage. The residual inherits every measurement error and omitted friction. Convenience yield is not a coupon deposited into an account and cannot always be arbitraged directly.

Shorting a commodity may require borrowing a particular grade at a particular location. Delivery options in the futures contract give the short choices that affect value. Perishability, seasonality, transport bottlenecks, and inventory capacity complicate the physical replication.

## Contract-creation lesson

When designing a derivative on a physical exposure, specify grade, location, delivery window, quality tolerance, and disruption rules. “One unit of oil” is not one economic object across pipelines and dates.

> **Memory seal:** the emergency barrel glows because ownership prevents a shutdown. A paper promise arriving later cannot provide today's service.

[Next: Basis and Convergence](../033-basis-and-convergence/README.md)
