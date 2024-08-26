
  ![Tech ROAD MAP Logo](assets/READMEN/Tech_roadmap_BB.png)
 

# Tech-Roadmap-DRF,

Tech-ROADMAP-DRF is a robust backend API built using Django with Django Rest Framework (DRF), designed to guide individuals who are eager to dive into the world of Information Technology (IT) but are unsure of where to start. Leveraging the power of Django's scalable architecture and the flexibility of DRF, this project serves as a comprehensive platform for delivering structured content, personalized learning paths, and community-driven resources to users.

The primary purpose of Tech-ROADMAP-DRF is to demystify the IT landscape for newcomers by offering a centralized hub of knowledge and guidance. Through a carefully curated collection of articles, courses.

With Tech-ROADMAP-DRF, users can navigate the often overwhelming array of IT disciplines—whether it's programming, cybersecurity, data science, or cloud computing—and find a clear, structured path to follow. By offering personalized course recommendations based on user preferences and progress, the project aims to create a tailored learning experience that empowers individuals to confidently embark on their IT journey.

In essence, Tech-ROADMAP-DRF harnesses the capabilities of Django and DRF to create a user-friendly backend system that not only delivers content but also fosters an interactive and supportive learning environment, making it an invaluable tool for aspiring IT professionals.

- [Tech-Roadmap-DRF,](#tech-roadmap-drf-)
- [Table of content](#table-of-content)
- [Planning](#planning)
- [Data Models](#data-models)
  * [ERD Diagram](#erd-diagram)
  * [Entitiy and Realtions](#entitiy-and-realtions)
- [API Endpoints](#api-endpoints)
- [Frameworks, Libraries and Dependencies](#frameworks--libraries-and-dependencies)
- [Testing](#testing)
  * [Manuel Testing](#manuel-testing)
  * [Python Validation](#python-validation)
  * [Bugs](#bugs)
    + [Unresolved Bugs](#unresolved-bugs)
    + [Resolved Bugs](#resolved-bugs)
- [Deployment](#deployment)
- [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Planning

## Objectives

1. **Provide a Comprehensive IT Learning Platform**: Create a centralized resource that offers diverse IT-related articles.

2. **Enable Personalized Learning Paths**: Develop a system that recommends specialized courses and content targeting users' interests, experience levels to draw future career paths.

3. **Facilitate User Interaction and Engagement**: Implement features that allow users to comment, review, and rate content.

4. **Promote Knowledge Sharing**: Encourage users to contribute their insights, experiences, and feedback, enriching the platform with community-driven content and discussions.

5. **Ensure Secure User Authentication**: Implement a secure authentication system to an account which belongs to a certain user data and provide a personalized experience based on user profiles.

6. **Integrate Social Features**: Allow users to follow others, create connections , and build a network that supports collaborative learning.

7. **Optimize for Scalability and Performance**: Ensure the API is designed for high performance and scalability to accommodate a growing user base and expanding content library.

8. **Provide Comprehensive Documentation and API Support**: Offer detailed documentation for the API, making it easy for developers to integrate, extend, and contribute to the project.

## Allocated Time for Django Rest API

When I first come to the idea why should I develope an API tha is only accessible for the Admins, I didn't get the point clear enough that the API is just like a blue print which can be used to build different front end website based on the endpoints offered by this API. Developing an API that is accessible for Front-End Website is a game changer and that is why I tool some time to paln and implement the API using a walkthrough project by Code Institute 

**Coding the Backend DRF took me about 12 days WITHOUT README**

the **Timeline** looks like the following:

Day 1 : Intitialising the project on GitHub using the [procvided Code Institue template](https://github.com/Code-Institute-Org/ci-full-template) provided. Cloning the Project on the Visual Studio IDE locally and set up environment variables.

Day 2: Designing the Database in its primary structure and required entities. Models shown in this project are designed on [Qucik Database Diagram](https://app.quickdatabasediagrams.com/#/d/qGYihO)

Day 3: Normalising the Relationship between the different entities any models. 

Day 4 till Day 10: This period is the coding time where I used the Code Institue walkthrough project to tailor my project. Afterwards, I did add more models to my project which will enhance the user experience about the exapnding and extending the project. The new modesl like (Category, Course, Review and Rating) are coded to target users who want not just to read, comment and review the available articles but instead take them a step further to choose a course and go for it. If the course provided helped them, they will be able to write their review and rate it. It helps other users to make decision better on the experience of other participants. It is also worth mentioning that during the coding stage I make a use of new skills gained from the walkthrough project. Refactoring the code is one of the main and major skills to reduce the amount of code and reaching the same final result. Finally, I applied the filter mechanism to some of the models and left someother to be like a future feature when other programmers will deploy this API and make some changes to their cloned copy of this API. 

Day 11 and day 12: Deployment on Heroku Platform: preparing the project when it is API requires migrating the Database which is designed and implementing locally using SQLite. I took the following steps:

1. Updainting the ALLOWED_HOSTS variable.
2. Moving sensitive data to env.py
3. Installing extra packages for authentication
4. Installing the TOKEN packages
5. Editing the settings.py file with TOKEN varibales
6. Editing the urls.py file of the root project
7. Freezing the dependencies into the requirement.txt file
8. Creating the PocFile which is required on the HEROKU Platform
9. Creating the Database on PostGRES and link it into the project settings.py file
10. Setting a new App on Heroku Platform
11. Link the App Source to GitHub
12. Creating the Varibale from the env.py on HEROKU 
13. Manuelly deploying the project.

**Deployment on Heroku** will be explained in a later section

**Writing the README** starts after deployment of this API which is not recommend because it would be tedious work, though it presents a big and complete project to explain and dive into its details.

# Data Models

In the Tech-ROADMAP-DRF API, the architecture is built around several interconnected models that collectively form the backbone of the platform. These models are designed to create a comprehensive and interactive environment for users exploring the IT world. The Walkthrough project provided the following Models User, Profile, Posts, Comment, Like and Follower. I changed the Post to be Article and added some new Models including Course, Review and Rating models. 

Together, these models create an integrated ecosystem within Tech-ROADMAP-DRF, offering users a personalized and engaging experience as they navigate through various IT disciplines.

## Database Models

The database schema is meticulously designed to optimize data storage, retrieval, and relationships among various entities. Leveraging Django's ORM (Object-Relational Mapping), it establishes a robust and scalable database architecture. The schema integrates both Django's built-in models and custom-designed models tailored to meet the specific needs of the diving center application.

## Entity Relational Diagram (ERD):

In the Tech-ROADMAP-DRF API, the data architecture is built on a collection of interconnected models that work together to provide a seamless and interactive experience for users. These models are structured using Django's Models, ensuring a scalable and efficient system that supports various functionalities of the platform. I used [Qucik Database Diagram](https://app.quickdatabasediagrams.com/#/d/qGYihO) for normalizing these entities:

![DRF_ERD_1](assets/READMEN/DRF_ERD_1.png)

## Architecture

1. User and Profile: The User model handles authentication and basic user information, while the Profile model extends it to include additional details like interests and preferences, creating a personalized user experience.

2. Article, Comment, and Like: The Article model is the core of the content system, storing educational articles across different IT fields. The Comment model allows users to engage with the content, while the Like model tracks user appreciation, fostering community interaction.
3. Follower: This model manages user relationships, enabling users to follow each other, which supports the social and collaborative aspect of the platform.
4. Course: Courses are structured learning paths that guide users through curated content in specific IT domains, helping them build knowledge systematically.
5. Review and Rating: These models ensure content quality by allowing users to review and rate articles and courses, helping others identify valuable resources quickly.

Together, these models form a well-organized and flexible architecture that powers the Tech-ROADMAP-DRF platform, supporting its goal of guiding users through their IT learning journey.

## Logic Through ERD
Based on the User interests, the shown entities are connected together to show a different front end provided by the defined field of interest. For example, when a user visit the website, a neutral view will be shown based on the date of article posted, though if a user choosed to like that article, the category entity will come into play to start showing articles of that kind. This logic is achieved by tracking users Likes and Following actions .

Users will be show all available courses filtered also based on the field of interest. Before choose to go for a course, User can read the Course Review and check its Rating making sure that the course meets exactly his intesntion. The relationship betweeen the different entities on the API side makes it possible to track, view and build different Front-End templates.

**Following is a descritpion about the implemented Models**

### User MOdel

The User model in Django Rest Framework (DRF) is a core component of the authentication and user management system. It is based on Django's built-in User model, which is provided by the django.contrib.auth module. This model is essential for handling user authentication, permissions, and managing basic user information such as usernames, passwords, and email addresses.

**Core Features of User Model**

1. **Authentication:** The User model is integral to the authentication system, allowing users to securely log in and access protected areas of the application. It supports various authentication methods, including token-based authentication, session-based authentication, and OAuth.

2. **Password Management:** The User model includes built-in mechanisms for securely storing passwords using hashing algorithms. Django also provides password reset and change functionalities, making it easier to manage user credentials.

3. **Permissions and Groups:** The User model supports assigning permissions and groups to users. This allows fine-grained control over what actions a user can perform within the application. The is_staff and is_superuser flags are examples of permissions used to control access to the Django admin interface and other restricted areas.

**Relation to the Profile Model**

In many applications, the default fields provided by the User model may not be sufficient to capture all the necessary information about a user. This is where the **Profile model** comes into play. The Profile model extends the User model by storing additional data that is not part of the core user model.

### Profile Model

The Profile model is an extension of the core User model, designed to store additional user-specific information that goes beyond basic authentication and user management. It enriches the user experience by allowing for more detailed personal profiles, which can be customized to fit the needs of the application.

### Key Features of the Profile Model

1. **One-to-One Relationship with User**: The `owner` field establishes a one-to-one relationship with the User model using Django's `OneToOneField`. This ensures that each user has a unique profile, directly linked to their account, and allows easy access to extended user data.

2. **Nickname**: The `nickname` field allows users to set a nickname, providing a more personalized identifier within the platform. This can be used in place of the username in social features, comments, and user interactions.

3. **About Section**: The `about` field offers users the ability to write a brief description or bio about themselves. This optional field helps users express their interests, background, or any other relevant information they wish to share.

4. **Timestamps**: The `created_at` and `updated_at` fields automatically record when the profile was created and last updated. These timestamps help track profile activity and modifications, ensuring the profile information is current.

5. **Profile Image**: The `image` field allows users to upload a profile picture, which enhances personalization and visual identification across the platform. If no image is provided, a default profile image is used.

### Relation to the User Model

The Profile model is tightly coupled with the User model, providing a way to extend and customize user data without altering the core User model itself. This separation of concerns ensures that authentication and user management remain focused and efficient, while the Profile model handles all additional user attributes that enhance the overall user experience.
