# Domain Model

## Core Entities

- Factory
- Department
- Machine
- User
- Team
- Case
- Observation
- Investigation
- Solution
- Lesson Learned
- Knowledge Asset
- AI Recommendation
- Report
- Notification

---

## Relationships

Factory
└── Departments

Department
└── Machines

Machine
└── Cases

Case
├── Observations
├── Investigations
├── Solutions
└── Lessons Learned

Knowledge Asset
└── Generated from Case

User
└── Creates Observations

AI Recommendation
└── Attached to Case