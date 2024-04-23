Capstone project for AWS

Backend Development for To-Do App

1. Introduction:
In this capstone project, your team will create the backend server to support a To-Do app.
The To-Do app is a web application that allows users to manage their tasks and todo lists.
The frontend of the application has been developed using HTML, CSS, and JavaScript, as demonstrated in class:

The backend development team is tasked with implementing the server-side functionality to support the To-Do app.
This document outlines the requirements and specifications for the backend development.

2. Functional Requirements:
The backend server should provide APIs to manage tasks and implement CRUD
operations for these tasks.
- 2.1 Create Task API
The server shall provide an API for creating a new task.
The API shall accept a POST request with the task details in the payload. You can expect
the payload to be the following:
{
"id": 4,
"name": "Finish project",
"category": "Work",
"dueDate": "2024-03-30"
}
The API shall validate the task details before saving them to the database.
The API shall return a response with the created task details.
- 2.2 Update Task API
The server shall provide an API for updating an existing task.
The API shall accept a PUT request with the updated task details in the payload.
The API shall validate the updated task details before saving them to the database.
The API shall return a response with the updated task details.
- 2.3 Delete Task API
The server shall provide an API for deleting an existing task.
The API shall accept a DELETE request with the task id in the payload.
The API shall delete the task with the given id from the database.
The API shall return a response confirming the deletion of the task.
- 2.4 Retrieve Tasks API
   - The server shall provide an API for retrieving all tasks.
The API shall accept a GET request.
The API shall return a response with all the tasks in the database.
- 2.5 Data Storage:
Use a suitable database to store user account information and tasks.

3. Non-Functional Requirements:
- 3.1 Scalability:
Design the backend system to be scalable, allowing it to handle increased user loads.
Leverage scalable AWS cloud services for hosting the backend infrastructure.
Implement load balancing and auto-scaling mechanisms to distribute traffic evenly and handle spikes in user activity.
- 3.2 Reliability:
Implement error handling and logging to track and diagnose issues.
Backup user data regularly to prevent data loss.

4. Deployment and Testing:
- Develop a deployment strategy for deploying the backend services to production.
- Implement automated testing (unit tests, integration tests) to ensure the reliability and correctness of backend functionality.
- Use continuous integration and continuous deployment (CI/CD) pipelines for automated testing and deployment processes.

5. Documentation:
- Provide comprehensive documentation for backend APIs, including endpoints, request/response formats.
- Maintain up-to-date documentation for future reference and onboarding of new team members.

6. Conclusion:
The successful implementation of the backend requirements outlined in this documentwill enable the To-Do app to provide users with a secure, reliable, and efficient task
management solution. The backend development team is responsible for ensuring that all functional and non-functional requirements are met, and for delivering a high-quality
backend system that seamlessly integrates with the frontend.
======================================================================

Assessment Criteria
The project will be assessed based on the following:
Part 1 – Demonstration of Solution (40%)
Part 2 – Presentation (30%)
Part 3 – Report (30%)
Part 1 – Demonstration of Solution (40%)
This assesses the functionality and usability of the backend system in action. Your team
should showcase the implemented features of the backend, and in particular the CRUD
operations.
You can provide examples of API requests using tools like Postman, Insomnia, or cURL.
