# AI Agent Notes

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Purpose: Handoff notes for future architecture or implementation work.

## Current Understanding

The user provided a raw idea, not an existing system.

The proposed system is for tennis court booking with coaches, member
discounts, payments, and admin management.

## User-Provided Facts

- Tennis court booking is required.
- Coaches are in scope.
- Member discounts are in scope.
- Payments are in scope.
- Admin management is in scope.

## Assumptions

- Members have accounts or identifiers.
- Payments use an external provider.
- Admins manage courts, coaches, bookings, pricing, and discounts.
- Payment is required before booking confirmation.

## Proposed Architecture Status

- All modules, workflows, entities, and diagrams are proposed.
- No implementation exists in the provided context.
- No provider, database, framework, or deployment target has been approved.

## Open Questions

- Are coaches booked with courts, separately, or both?
- How are member discounts calculated?
- Is payment required before booking confirmation?
- Are refunds, cancellations, and recurring bookings in scope?
- Can guests book without accounts?

## Risks

- Double booking without conflict rules.
- Payment and booking state mismatch.
- Unclear discount eligibility.
- Over-broad admin permissions.

## Decisions Requiring Approval

- Booking lifecycle.
- Coach booking model.
- Member identity model.
- Payment provider and refund scope.
- Admin role and audit requirements.

## Safe Next Actions

- Ask the blocking questions before implementation planning.
- Review assumptions with the user.
- Keep all architecture labeled as proposed until approved.

## Avoid Until Clarified

- Do not select a payment provider.
- Do not design final database schema.
- Do not implement booking logic.
- Do not claim any module exists.
