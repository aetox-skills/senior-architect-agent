# Open Questions

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Source: User-provided raw idea.

## User-Provided Facts

- Courts can be booked.
- Coaches, member discounts, payments, and admin management are in scope.

## Assumptions

- Members need a way to identify themselves.
- Payments are handled by an external provider.
- Admins can manage availability and operational records.

## Blocking

| Question | Why It Matters | Status |
| --- | --- | --- |
| Are coaches booked with courts, separately, or both? | Changes module boundaries and workflow. | Open |
| Is payment required before booking confirmation? | Changes booking state and payment flow. | Open |
| How are member discounts calculated? | Changes pricing and data model. | Open |

## Important

| Question | Why It Matters | Status |
| --- | --- | --- |
| Are refunds and cancellations required? | Changes payment and booking lifecycle. | Open |
| Can admins override bookings or discounts? | Changes admin permissions. | Open |
| Are recurring bookings required? | Changes scheduling complexity. | Open |

## Useful

| Question | Why It Matters | Status |
| --- | --- | --- |
| Which payment provider is preferred? | Affects integration design. | Open |
| Should guests book without accounts? | Affects identity model. | Open |

## Decisions Requiring Approval

- Booking confirmation rule.
- Coach booking model.
- Discount calculation model.
- Payment provider and refund scope.

## Next Steps

- Resolve blocking questions before implementation planning.
- Continue with explicit assumptions only for proposal review.
