# Project Kickoff File – GordiBurg

## Application Name:
**GordiBurg** – Food ordering app specializing in burgers and street food

---

## Project Budget

**Total budget available:** 50,000 MXN (Mexican Pesos)

### Budget Breakdown:

| Area                         | Estimated Amount (MXN) | Description                                                              |
|-----------------------------|-------------------------|--------------------------------------------------------------------------|
| Mobile frontend development | 15,000                  | Android app (customer-facing interface)                                  |
| Backend development         | 12,000                  | RESTful API, authentication, database, business logic                    |
| Infrastructure (AWS)        | 8,000                   | Hosting, database, storage, monitoring                                   |
| Admin web interface         | 5,000                   | Web panel to manage products, orders, and users                          |
| Testing and QA              | 4,000                   | Unit testing, integration testing, user experience testing               |
| Graphic design and marketing| 3,000                   | Visual branding and initial promotion                                    |
| Contingency fund            | 3,000                   | Reserved for unforeseen events or future improvements                    |

---

## ADR - Architectural Decision Record

**Title:** Architecture selection for a food ordering application  
**Status:** Accepted  
**Date:** 2025-05-29  

### Context:

The GordiBurg app is a mobile platform focused on facilitating fast food orders, allowing users to:

- Register and log in  
- Browse the product menu  
- Place and confirm orders  
- Receive immediate confirmation of their order

---

### Decision:

A modern architecture has been chosen consisting of:

#### Mobile Frontend (Android):
- Registration and login screen
- Menu screen displaying at least 3 products
- Order selection and confirmation flow

#### Backend:
- Authentication and authorization modules
- User, product, and order management
- Secure REST API


## Initial Validations

### 1. User Registration
- Account creation with email and password validation
- Login and session control for users

### 2. Product Menu
- Display of at least 3 products, each with name, price, image, and order button
- Optional basic filtering or categorization

### 3. Welcome Message / Order Placement
- Personalized greeting after successful login
- Selection and confirmation of an order, with a success message displayed

---

## Justification for Using an External Resource (AWS)

Using **Amazon Web Services (AWS)** is recommended for the following reasons:

- **Scalability:** supports increasing computing needs without restructuring the app
- **High availability:** ensures the system is always accessible
- **Security:** controlled access, SSL certificates, and automatic backups
- **Built-in monitoring:** CloudWatch for metrics and CloudTrail for auditing
