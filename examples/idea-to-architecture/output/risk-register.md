# Risk Register

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Source: User-provided raw idea.

## User-Provided Facts

- Booking, coaches, member discounts, payments, and admin management are in
  scope.

## Assumptions

- Payments use an external provider.
- Discounts depend on member identity.
- Admin actions change operational data.

## Risks

| Risk | Why It Matters | Status | Mitigation |
| --- | --- | --- | --- |
| Double booking | Courts and coaches need conflict rules. | Proposed risk | Define locking rules. |
| Payment mismatch | Payment and booking states can diverge. | Proposed risk | Define lifecycle states. |
| Discount ambiguity | Member rules may be unclear. | Proposed risk | Approve discount model. |
| Admin overreach | Admins can change sensitive data. | Proposed risk | Define roles and audit needs. |
| Refund uncertainty | Refund scope is unknown. | Proposed risk | Decide cancellation policy. |

## Unknowns

- Payment provider.
- Refund and cancellation policy.
- Member tiers and discount stacking.
- Coach scheduling rules.
- Admin role levels.

## Decisions Requiring Approval

- Whether to support unpaid holds.
- Whether refunds are in initial scope.
- Whether admin audit logs are required.
- Whether guests can book.

## Next Steps

- Resolve payment and booking lifecycle questions.
- Approve discount and identity assumptions.
- Reassess risks after scope decisions.
