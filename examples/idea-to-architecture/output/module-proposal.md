# Module Proposal

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Status: Proposed, not implemented.

## User-Provided Facts

- The system includes booking, coaches, member discounts, payments, and admin
  management.

## Assumptions

- The backend owns booking and pricing rules.
- The payment provider is external.
- Admin management is a protected workflow.

## Proposed Modules

| Module | Responsibility | Depends On | Status |
| --- | --- | --- | --- |
| Booking | Court availability, reservations, booking states. | Pricing, Payment | Proposed |
| Coach | Coach profiles, schedules, assignment rules. | Booking | Proposed |
| Pricing | Base prices, member discounts, totals. | Member data | Proposed |
| Payment | Payment intent, status, provider callbacks. | Booking, Provider | Proposed |
| Admin | Manage courts, coaches, bookings, discounts. | All domain modules | Proposed |
| Identity | Members, admins, and access control. | None selected | Proposed |

## Proposed Shared Modules

| Module | Responsibility | Status |
| --- | --- | --- |
| Notification | Booking and payment messages. | Optional |
| Audit log | Admin action traceability. | Optional |

## Decisions Requiring Approval

- Whether identity is required for guests.
- Whether coach booking is part of booking or a separate module.
- Whether notifications are in initial scope.
- Whether audit logging is required for admins.

## Open Questions

- Can one booking include multiple courts or coaches?
- Can members have different discount tiers?
- Can admins manually mark payments as resolved?

## Risks

- Combining booking, coach scheduling, and payments too tightly may make later
  changes harder.
- Weak identity rules may make member discounts unreliable.

## Next Steps

- Approve module boundaries.
- Define booking lifecycle states.
- Decide optional shared modules.
