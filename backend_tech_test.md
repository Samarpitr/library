# Tech Test Brief: Backend Python Engineer

Your task is to create a simple RESTful API using FastAPI that allows users to perform CRUD (Create, Read, Update, Delete) operations on a resource called "books".

Requirements:
1. Implement the following endpoints:
    - GET /books: Retrieve a list of all books.
    - GET /books/{id}: Retrieve a specific book by its ID.
    - POST /books: Create a new book.
    - PUT /books/{id}: Update an existing book by its ID.
    - DELETE /books/{id}: Delete a book by its ID.
2. The book resource should have the following attributes:
    - ID (integer): Unique identifier for the book.
    - Title (string): Title of the book.
    - Author (string): Author of the book.
    - Publication Year (integer): Year the book was published.
3. Use appropriate data validation and error handling techniques.
4. Store the book data in memory (no need for a database).
5. Write unit tests to ensure the functionality of your API.

## Additional Notes:
- You are free to structure your code and project as you see fit.
- Feel free to use any additional libraries or tools that you think are necessary.
- Provide clear instructions on how to run and test your API.

## Evaluation Criteria:
- Correctness: Does the API meet the specified requirements?
- Code Quality: Is the code well-structured, readable, and maintainable?
- Error Handling: Does the API handle errors gracefully?
- Testing: Are there sufficient unit tests to validate the functionality?

## Bonus points (but NOT required) for making use of the following tools/technologies

- Docker
- Postgres
- Async python
- Type annotations
- pytest
- sqlmodel

## Submission:
- Provide a link to a GitHub repository containing your code.
- Include a README file with instructions on how to run and test your API.

Good luck!
