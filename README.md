# Movie Subscription Access System (MSAS)

## 📌 Project Overview

The **Movie Subscription Access System (MSAS)** is a backend API built with **Django and Django Rest Framework (DRF)** that manages user authentication, subscriptions, and controlled access to movie content for a streaming platform.

The system ensures that:

* Only authenticated users can subscribe
* Users with **active subscriptions** can access premium movie content
* Users are **not double-billed** when they already have an active subscription

This project is designed as a **production-ready backend service**, suitable for real-world deployment and frontend integration.

---

## 🚀 Live Deployment

**Base URL:**

```
https://lordes.pythonanywhere.com/api/auth/login
```

---

## 🛠 Tech Stack

* **Backend:** Django, Django Rest Framework (DRF)
* **Authentication:** JWT (SimpleJWT)
* **Database:** SQLite
* **Deployment:** PythonAnywhere
* **Language:** Python 3.10

---

## 🔐 Authentication Flow (JWT)

1. User registers
2. User logs in
3. API returns **access & refresh tokens**
4. Frontend stores access token
5. Protected endpoints require:

---

## 👤 Users Module

### Features

* User registration
* User login (JWT-based)
* User profile management
* Admin-controlled user listing

### Endpoints

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| POST   | `/api/auth/register/` | Register new user       |
| POST   | `/api/auth/login/`    | Login & get JWT tokens  |
| GET    | `/api/auth/users`     | List users (Admin only) |

---

## 💳 Subscriptions Module

### Features

* Start subscription
* Renew subscription
* Check subscription status
* Prevent duplicate active subscriptions

### Subscription Logic

* Subscriptions last **30 days**
* Renewal extends the `end_date`
* Active status is checked using current date

### Endpoints

| Method | Endpoint                    | Description                 |
| ------ | --------------------------- | --------------------------- |
| POST   | `/api/subscriptions/start/` | Start new subscription      |
| POST   | `/api/subscriptions/renew/` | Renew existing subscription |
| GET    | `/api/subscriptions/check/` | Check active subscription   |

*(Authentication required)*

---

## 🎬 Movies Module

### Features

* Public movie listing
* Movie search
* Genre-based organization
* Access control for movie streaming

### Endpoints

| Method | Endpoint                  | Access                     |
| ------ | ------------------------- | -------------------------- |
| GET    | `/api/movies/`            | Public                     |
| GET    | `/api/movies/search/`     | Public                     |
| GET    | `/api/genres/`            | Public                     |
| GET    | `/api/movies/{id}/watch/` | Auth + Active Subscription |

---

## 🔒 Access Control Logic

* Public users can browse movies
* Only authenticated users can request to watch a movie
* Only users with **active subscriptions** can access the watch endpoint
* Unauthorized access returns `401 / 403`

---

## ✅ Project Status

✔ Fully functional backend
✔ Production deployed
✔ Secure authentication
✔ Ready for frontend integration

---

## 📈 Possible Future Improvements

* Payment integration (Paystack / Stripe)
* Frontend UI (React / Next.js)
* Recommendation system
* Watch history & analytics

---

## 👨‍💻 Author

**Clement Odeh**
Backend Developer | Mechanical Engineer
Focused on building practical systems that solve real-world problems.

---

## 📄 License

This project is for educational and portfolio purposes.
