# Architecture Proposal

## Scope

- Idea: Tennis court booking system.
- Mode: Idea-to-Architecture Mode.
- Status: Proposed, not implemented.
- Source: User-provided raw idea.

## User-Provided Facts

- The system needs bookings, coaches, member discounts, payments, and admin
  management.

## Assumptions

- The system is a web application.
- Users can view availability before booking.
- Members are identified so discounts can be applied.
- Payments are processed by an external payment provider.
- Admins manage courts, coaches, pricing, discounts, and booking records.

## Proposed Architecture

Propose a web application with a frontend, backend API, booking service,
pricing and discount service, coach management, payment integration, admin
module, and database.

All components are proposed and require approval before implementation.

## Design Rationale

- A frontend app is proposed because guests, members, and admins need distinct
  interaction surfaces.
- A backend API is proposed to keep booking, pricing, payment, and admin rules
  outside the UI.
- Separate booking, coach, and pricing services are proposed because court
  availability, coach scheduling, and discounts can change independently.
- A payment adapter is proposed to isolate external payment provider details.
- A database is proposed because bookings, members, discounts, and payments need
  durable records.

## Proposed Components

| Component | Responsibility | Status |
| --- | --- | --- |
| Frontend app | Booking, member, coach, and admin UI. | Proposed |
| Backend API | Coordinates booking, pricing, payment, and admin actions. | Proposed |
| Booking service | Owns court availability and booking lifecycle. | Proposed |
| Coach service | Owns coach schedules and assignment rules. | Proposed |
| Pricing service | Calculates prices and member discounts. | Proposed |
| Payment adapter | Integrates with an external payment provider. | Proposed |
| Admin module | Manages courts, coaches, discounts, and bookings. | Proposed |
| Database | Stores users, courts, coaches, bookings, payments, discounts. | Proposed |

## Proposed Boundary

```mermaid
flowchart LR
  User[Guest or Member] --> Frontend[Frontend App]
  Admin[Admin] --> Frontend
  Frontend --> API[Backend API]
  API --> Booking[Booking Service]
  API --> Coach[Coach Service]
  API --> Pricing[Pricing Service]
  API --> AdminModule[Admin Module]
  API --> Payment[Payment Adapter]
  Booking --> DB[(Database)]
  Coach --> DB
  Pricing --> DB
  AdminModule --> DB
  Payment --> Provider[Payment Provider]
```

## Tradeoffs

- Separate booking and pricing modules keep rules clearer but add coordination.
- External payments reduce payment risk but add provider dependency.
- Member accounts simplify discounts but may increase onboarding friction.

## Open Questions

- Are coach bookings tied to court bookings?
- What booking states are required?
- Which payment provider should be used?
- Are refunds and cancellations in scope?

## Risks

- Booking and payment state may diverge without clear lifecycle rules.
- Discounts may become complex if member tiers or promotions are added later.
- Admin permissions may be too broad without role definitions.

## Decisions Requiring Approval

- Proposed component boundaries.
- Payment-before-confirmation rule.
- Account requirement for members and guests.
- Admin role scope.

## Next Steps

- Review the proposed boundary.
- Resolve blocking questions.
- Produce an implementation plan only after approval.
