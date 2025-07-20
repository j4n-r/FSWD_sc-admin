---
title: Design Decisions
nav_order: 3
---

{: .label }
Jan Rueggeberg

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: How to access the database?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

Should we perform database CRUD (create, read, update, delete) operations by writing plain SQL or by using SQLAlchemy as object-relational mapper?

### Decision

We stick with plain SQL since the application is not complex enough to justify learning an ORM. 
This decision was made by Jan Rueggeberg.

### Regarded options

We regarded two alternative options:

+ Plain SQL
+ SQLAlchemy

Why plain SQL?
+ The team already knows SQL
+ The queries are simple enough 
+ Overhead to learn SQLAlchemy is not worth it and will create unnecessary complexity for this use case (since we already have simple queries)
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

The decision was made to use Blueprints due to overrating the complexity of the app by Jan Rueggeberg. It will not be revised since the result is still valid if the application should grow.

### Regarded options

The decision to use Blueprints was made because it brings better modularity for the cost of some added complexity. 
This was not needed for a project of this complexity level (having only two blueprints at the moment). But since the refactoring would make no sense, meaning that if the application would grow, having it split in blueprints is probably a pleasant thing, this decision will stay.

## 03: Which styling framework should we use?

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-06-2025

### Problem statement

What styling approach should be used for the application's front-end? The main options are a component-based framework like Bootstrap 5 or a utility-first framework like Tailwind CSS.

### Decision

The decision was made by me (Jan Rueggeberg) to use Tailwind CSS. The primary reason is significantly higher development speed for myself, while other team members have no strong preference or prior experience with other frameworks that would be negatively impacted.

### Regarded options

We regarded two main options for the styling framework:

+ Tailwind CSS
+ Bootstrap 5

With https://flowbite.com/docs/components/ we can have a more modular approach with the additional flexibility of Tailwind CSS. 
Using both styling options at the same time did not work because of the style resets. That would've been also really messy.

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

Integrating the websocket server into the flask app would be the easier and more time efficient solution. The performance loss of using Python vs Rust is not relevant since the app has no users and switching later to a standalone one would not really be a problem.

Why still build something else?

Since I am learning Rust at the moment and it brings me more joy learning this new shiny thing than quickly writing it in Python I have decided to write a standalone application.
I am sure that the scope of this project is still big enough for the coursework. 
The only real negative is that it makes running the whole project a bit more tricky, but I think I managed that well enough with the run.sh script.

## 05: Should we use WTForms

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 21-06-2025

### Problem statement

Should we use the WTForms library for managing forms or handle them with plain HTML and Flask request handling?

### Decision

We are not using WTForms. 

### Regarded options

We regarded two options:

+ WTForms
+ Plain HTML forms

Why plain HTML forms?
+ WTForms is too much "magic" - adds unnecessary abstraction layer
+ Jan R. already knows normal HTML forms
+ CSRF validation is nice but this is not a critical application
+ Server side validation is not needed since only admin users use the forms
+ Faster development without learning additional framework
+ Full control over form styling and behavior
+ No additional dependencies

The overhead of learning WTForms is not justified for simple forms in this application.
