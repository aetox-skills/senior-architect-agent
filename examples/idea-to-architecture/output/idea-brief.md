# Idea Brief

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Source: User-provided raw idea.
- Status: Proposed architecture draft.

## User-Provided Facts

- The system should support tennis court booking.
- The system should include coaches.
- The system should support member discounts.
- The system should support payments.
- The system should include admin management.

## Inspection Limitations

- No existing implementation was provided.
- No source files, schema, payment provider, or deployment target were provided.
- Business rules are unknown unless listed as user-provided facts.

## User Intent

- Provide a way to reserve tennis courts.
- Include coach-related scheduling or management.
- Apply member discounts.
- Accept payments.
- Let admins manage operational data.

## Assumptions

- Members have accounts or identifiers for discount eligibility.
- Courts have time slots that can be booked.
- Coaches can be scheduled by users or managed by admins.
- Payments use an external provider rather than a custom payment system.
- Admins manage courts, coaches, bookings, discounts, and payment visibility.

## Proposed Actors

| Actor | Need | Status |
| --- | --- | --- |
| Guest | Browse availability or start a booking. | Proposed |
| Member | Book with possible discounts. | Proposed |
| Coach | Be scheduled or managed. | Proposed |
| Admin | Manage courts, coaches, prices, and bookings. | Proposed |
| Payment provider | Process payments. | Proposed |

## Open Questions

- Are coaches booked with courts, separately, or both?
- Do member discounts apply to courts, coaching, or the full order?
- Is payment required before a booking is confirmed?
- Are refunds and cancellations in initial scope?

## Decisions Requiring Approval

- Whether the system needs user accounts for all bookings.
- Whether coaches are independent bookable resources.
- Which payment provider or payment flow should be used.
- Which admin capabilities are required first.

## Next Steps

- Answer the blocking architecture questions.
- Approve or revise the proposed assumptions.
- Convert approved decisions into an implementation plan later.
