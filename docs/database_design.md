 # Database Design

## Factory

* id
* name
* location
* industry_type
* created_at
* updated_at

---

## Department

* id
* name
* factory_id
* created_at

---

## Machine

* id
* name
* serial_number
* model
* manufacturer
* machine_type
* location_inside_factory
* department_id
* installation_date
* status
* created_at

---

## User

* id
* first_name
* last_name
* email
* role
* department_id
* created_at

---

## Case

* id
* title
* description
* case_type
* machine_id (Nullable)
* created_by
* priority
* severity
* status
* estimated_cost
* downtime_hours
* created_at
* closed_at

---

## Case Assignment

* id
* case_id
* user_id
* assignment_role
* assigned_at

---

## Observation

* id
* case_id
* user_id
* observation_text
* attachment
* created_at

---

## Comment

* id
* case_id
* user_id
* comment
* created_at

---

## Investigation

* id
* case_id
* engineer_id
* findings
* created_at

---

## Solution

* id
* case_id
* solution_text
* implemented_by
* implemented_at

---

## Knowledge Asset

* id
* case_id
* summary
* root_cause
* solution
* lessons_learned
* keywords
* review_status
* reviewed_by
* published_at

---

## Knowledge Tag

* id
* name

---

## AI Recommendation

* id
* case_id
* recommendation
* confidence_score
* generated_at

---

## Report

* id
* title
* report_type
* generated_by
* generated_at

---

## Notification

* id
* user_id
* title
* message
* is_read
* created_at

---

# Relationships

## Factory

One Factory
→ Has Many Departments

---

## Department

One Department
→ Has Many Machines

One Department
→ Has Many Users

---

## Machine

One Machine
→ Has Many Cases

---

## User

One User
→ Can Create Many Cases

One User
→ Can Write Many Observations

One User
→ Can Write Many Comments

One User
→ Can Lead Many Investigations

One User
→ Can Receive Many Notifications

---

## Case

One Case
→ Belongs To One Machine (Optional)

One Case
→ Has Many Case Assignments

One Case
→ Has Many Observations

One Case
→ Has Many Comments

One Case
→ Has One Investigation

One Case
→ Has One Solution

One Case
→ Generates One Knowledge Asset

One Case
→ Can Have Many AI Recommendations

---

## Knowledge Asset

One Knowledge Asset
→ Originates From One Case

One Knowledge Asset
→ Has Many Knowledge Tags

---

# Relationship Types

Factory (1) -------- (N) Department

Department (1) -------- (N) Machine

Department (1) -------- (N) User

Machine (1) -------- (N) Case

User (1) -------- (N) Case

Case (1) -------- (N) Case Assignment

Case (1) -------- (N) Observation

Case (1) -------- (N) Comment

Case (1) -------- (1) Investigation

Case (1) -------- (1) Solution

Case (1) -------- (1) Knowledge Asset

Case (1) -------- (N) AI Recommendation

Knowledge Asset (N) -------- (N) Knowledge Tag
