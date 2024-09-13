# Tech-Roadmap-DRF


## API Testing Overview

In this section, we will test the **CRUD** (Create, Read, Update, Delete) functionality for each model in the **Tech-Roadmap** API. The models we will be testing include **Profiles**, **Article**, **Comment**, **Follower**, **Likes**, **Course**, **Rating**, **Enrollment**, and **Review**. For each model, we will explore the available endpoints, their specific functions, and the expected responses. This will ensure that the API works as intended and supports all necessary operations for the platform.


- [Tech-Roadmap-DRF](#tech-roadmap-drf)
  * [API Testing Overview](#api-testing-overview)
    + [Profiles API Endpoints](#profiles-api-endpoints)
    + [Article Model API Endpoints](#article-model-api-endpoints)
    + [Follower Model API Endpoints](#follower-model-api-endpoints)
    + [Comment Model API Endpoints](#comment-model-api-endpoints)
    + [Category Model API Endpoints](#category-model-api-endpoints)
    + [Course Model API Endpoints](#course-model-api-endpoints)
    + [Review Model API Endpoints](#review-model-api-endpoints)
    + [Rating Model API Endpoints](#rating-model-api-endpoints)
    + [Enrollment API Endpoints](#enrollment-api-endpoints)
    + [Administration and Authorization API Endpoints](#administration-and-authorization-api-endpoints)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


### Profiles API Endpoints

| Endpoint                     | Functionality                                                    | Result |
|------------------------------|------------------------------------------------------------------|--------|
| `profiles/`                  | Retrieves a list of all profiles.                                | Pass   |
| `profiles/<int:pk>/`         | Retrieves a specific profile based on its primary key (PK).      | Pass   |
| `profiles/<int:pk>/delete/`  | Deletes a specific profile based on its primary key (PK).        | Pass   |


### Article Model API Endpoints

| Endpoint                     | Functionality                                                                                                  | Result |
|------------------------------|----------------------------------------------------------------------------------------------------------------|--------|
| `articles/`                  | **Create:** Use the `POST` method to create a new article.<br>**Retrieve:** Use the `GET` method to retrieve a list of all articles. | Pass   |
| `articles/<int:pk>/`         | **Retrieve:** Use the `GET` method to retrieve a specific article based on its primary key (PK).                 | Pass   |


### Follower Model API Endpoints

| Endpoint                     | Functionality                                                                                                      | Result |
|------------------------------|--------------------------------------------------------------------------------------------------------------------|--------|
| `followers/`                 | **Create:** Use the `POST` method to create a new follower relationship.<br>**Retrieve:** Use the `GET` method to retrieve a list of all followers for a specific user. | Pass   |
| `followers/<int:pk>/`        | **Retrieve:** Use the `GET` method to retrieve a specific follower relationship based on its primary key (PK).<br>**Delete:** Use the `DELETE` method to delete a specific follower relationship. | Pass   |


### Comment Model API Endpoints

| Endpoint                     | Functionality                                                                                                   | Result |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| `comments/`                  | **Create:** Create a new comment, associating it with a specific article or post.<br>**Retrieve:** Get a list of all comments related to a particular article or post. | Pass   |
| `comments/<int:pk>/`         | **Retrieve:** Get a specific comment based on its primary key (PK).<br>**Update:** Modify the content of a specific comment.<br>**Delete:** Remove a specific comment. | Pass   |


### Category Model API Endpoints

| Endpoint                     | Functionality                                                                                                    | Result |
|------------------------------|------------------------------------------------------------------------------------------------------------------|--------|
| `category/`                  | **Create:** Create a new category.<br>**Retrieve:** Get a list of all categories.                                 | Pass   |
| `category/<int:pk>/`         | **Retrieve:** Get a specific category based on its primary key (PK).<br>**Update:** Modify the details of a specific category (e.g., name or description).<br>**Delete:** Remove a specific category. | Pass   |


### Course Model API Endpoints

| Endpoint                     | Functionality                                                                                                      | Result |
|------------------------------|--------------------------------------------------------------------------------------------------------------------|--------|
| `courses/`                  | **Create:** Create a new course.<br>**Retrieve:** Get a list of all courses.                                        | Pass   |
| `courses/<int:pk>/`         | **Retrieve:** Get a specific course based on its primary key (PK).<br>**Update:** Modify the details of a specific course (e.g., change the course name, description).<br>**Delete:** Remove a specific course. | Pass   |


### Review Model API Endpoints

| Endpoint                     | Functionality                                                                                                   | Result |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| `reviews/`                  | **Create:** Create a new review, associating it with a specific course.<br>**Retrieve:** Get a list of all reviews for a particular course. | Pass   |
| `reviews/<int:pk>/`         | **Retrieve:** Get a specific review based on its primary key (PK).<br>**Update:** Modify the content or rating of a specific review.<br>**Delete:** Remove a specific review. | Pass   |


### Rating Model API Endpoints

| Endpoint                     | Functionality                                                                                                   | Result |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|--------|
| `ratings/`                  | **Create:** Create a new rating, associating it with a specific course.<br>**Retrieve:** Get a list of all ratings for a particular course. | Pass   |
| `ratings/<int:pk>/`         | **Retrieve:** Get a specific rating based on its primary key (PK).<br>**Update:** Modify the rating value for a specific rating.<br>**Delete:** Remove a specific rating. | Pass   |


### Enrollment API Endpoints

| Endpoint                     | Functionality                                                                                                    | Result |
|------------------------------|------------------------------------------------------------------------------------------------------------------|--------|
| `enrollments/`              | **Create:** Create a new enrollment, associating it with a specific user and course.<br>**Retrieve:** Get a list of all enrollments for a particular user or course. | Pass   |
| `enrollments/<int:pk>/`     | **Retrieve:** Get a specific enrollment based on its primary key (PK).<br>**Update:** Modify the details of a specific enrollment (e.g., change the status or completion date).<br>**Delete:** Remove a specific enrollment. | Pass   |


### Administration and Authorization API Endpoints

| Endpoint                        | Functionality                                                                                                    | Result |
|---------------------------------|------------------------------------------------------------------------------------------------------------------|--------|
| `/`                             | This path points to a landing view function that serves as the root of the Tech-Roadmap-DRF API.                 | Pass   |
| `/admin/`                       | Django admin panel for managing your application's data models.                                                  | Pass   |
| `/api-auth/`                    | Authentication and authorization endpoints provided by Django REST Framework.                                   | Pass   |
| `/dj-rest-auth/logout/`         | Custom logout route (typically defined in `logout_route`).                                                        | Pass   |
| `/dj-rest-auth/`                | Endpoints for user registration, login, password reset, etc., provided by django-rest-auth.                      | Pass   |
| `/dj-rest-auth/registration/`   | Endpoints specifically for user registration, managed by django-rest-auth.                                        | Pass   |
