---
title: Design Decisions
nav_order: 3
---

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Title]

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

---

## 01: How to access the database?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

### Decision

We stick with plain SQL since the application is not complex enough to justify learing an ORM. 
This decision was made by Jan Rueggeberg.

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

Why plain SQL?
+ The team already knows SQL
+ The queries are simple enough 
+ Over head to learn SQL alchemy is not worth it and will create unecessary complexity for this use case (since we already have simple queries)
+ The query results are easy to work with since the schema is also simple

## 02: Should we use flask blueprints?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

Should we split the Application into different Blueprints. (https://flask.palletsprojects.com/en/stable/blueprints/) 
### Decision

The decisions was made to use Blueprints dueto overrating the complexity of the app by Jan Rueggeberg. It will not be revised since the result is still valid if the application should grow.

### Regarded options

The decision to use Blueprints was made because it brings better modularity for the cost of some added complexity. 
This was not needed for a project of this complexity level (having only two blueprints at the moment). But since the refactoring would make no sense, meaning that if the application would grow, having it split in blueprints is probably a pleasant thing, this decision will stay.

Of course. Here is the "Styling framework" section rewritten to match the style and detail of the other entries.

## 03: Which styling framework should we use?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

What styling approach should be used for the application's front-end? The main options are a component-based framework like Bootstrap 5 or a utility-first framework like Tailwind CSS.

### Decision

The decision was made by me (Jan Rueggeberg) to use Tailwind CSS. The primary reason is significantly higher development speed for myself , while other team members have no strong preference or prior experience with other frameworks that would be negatively impacted.

### Regarded options

We regarded two main options for the styling framework:

+ Tailwind CSS
+ Bootstrap 5

With https://flowbite.com/docs/components/ we can have a more modular approach with the additional flexibility of tailwindcss. 
Using both styling options add the same time did not work because of the style resets. That would've been also really messy.

## 04: Should the websocket server be a standalone application?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

Integrate the websocket server into the flask app or build a standalone one.

### Decision

The decision was made to build a standalone application by Jan Rueggeberg for personal reasons.

### Regarded options

+ Standalone application
+ Integrate into the flask app

Integrating the websocket server into the flask app would be the easier and more time efficient solution. The perfomance loss of using python vs rust is not relevant since the app has no users and switching later to a standalone one would be not really be a problem.

Why still build something else?

Since I am learning rust at the moment and it brings me more joy learing this new shiny thing than quickly writing it in python I have decided to write a standalone application.
I am sure that the scope of this project is still big enough for the coursework. 
The only real negative is that it makes running the whole project a bit more tricky, but I think I managed that well enough with the run.sh script.

---
