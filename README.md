# Project_4

## Booxploration

[**Link to Frontend Repo**](https://github.com/lind1125/project_4_frontend)

[**Deployed API**]()

---

### Technologies used:

  * Python
  * PostgreSQL
  * Peewee
  * Flask
  * flask-login
  * CORS

---

### General Approach


---

### Installation instructions:


---

### ERD (tentative)

https://lucid.app/lucidchart/invitations/accept/51e56d3e-d9a3-420e-a28d-4cc64767ac29

### Routes:


| Verb | Endpoint | Action |
| ----------- | ----------- | ----------- |
| GET | '/' | Home page |
| POST | 'api/v1/persons/register' | Register user |
| POST | 'api/v1/persons/login' | Login user |
| GET | 'api/v1/persons/logout' | Logout user |
| GET | 'api/v1/persons/profile' | View user profile |
| ------ | ----------- | ----------- |
| GET | 'api/v1/books/faves' | View faved books |
| POST | 'api/v1/books/addfave' | Add book to faved books |
| PUT | 'api/v1/books/faves/:id | Update faved book |
| DELETE | 'api/v1/books/faves/:id | Delete faved book |

