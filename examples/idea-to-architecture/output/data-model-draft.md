# Data Model Draft

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Status: Proposed draft, not implemented.

## User-Provided Facts

- The system needs courts, coaches, member discounts, payments, and admin
  management.

## Assumptions

- Members are represented as users with membership status.
- A booking reserves a court time and may include a coach.
- Payments are tracked separately from bookings.
- Discounts can be configured by admins.

## Proposed Entities

| Entity | Purpose | Example Fields | Status |
| --- | --- | --- | --- |
| User | Member or admin identity. | id, role, memberStatus | Proposed |
| Court | Bookable tennis court. | id, name, status | Proposed |
| Coach | Coach profile and availability. | id, name, status | Proposed |
| Booking | Court reservation. | id, userId, courtId, start, end, status | Proposed |
| Payment | Payment record. | id, bookingId, amount, status | Proposed |
| Discount | Member discount rule. | id, type, value, eligibility | Proposed |

## Proposed Relationships

| From | Relationship | To | Status |
| --- | --- | --- | --- |
| User | creates | Booking | Proposed |
| Booking | reserves | Court | Proposed |
| Booking | may include | Coach | Proposed |
| Booking | has | Payment | Proposed |
| Discount | applies to | User or Booking | Proposed |

## Unknowns

- Whether guests can book without user accounts.
- Whether coaches have independent calendars.
- Whether discounts stack or expire.
- Whether refunds need separate records.

## Risks

- A weak booking status model can make payment reconciliation difficult.
- Discount rules can become ambiguous without eligibility definitions.
- Coach availability may conflict with court availability.

## Decisions Requiring Approval

- Required user identity model.
- Booking status lifecycle.
- Discount eligibility rules.
- Payment and refund record shape.

## Next Steps

- Approve proposed entities.
- Define booking lifecycle.
- Decide whether refund and cancellation models are required now.
