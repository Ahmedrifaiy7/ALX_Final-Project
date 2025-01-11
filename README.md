Recipe Management API

Description: The Recipe Management API is a Django REST Framework (DRF) application designed for managing recipes. It allows users to create, read, update, and delete recipes while providing functionalities like user authentication, filtering by category or ingredient, and searching recipes.

Features: User Authentication (with JWT Tokens) CRUD operations for users and recipes Search recipes by title, category, or ingredients Filter recipes by preparation time, cooking time, or category View recipes by category or ingredient Pagination and sorting for large datasets

Setup Instructions

Clone the Repository bash git clone cd recipe-management-api
Create a Virtual Environment bash python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate
Install Dependencies bash pip install -r requirements.txt
Set Up Environment Variables Create a .env file in the project directory and add:
env SECRET_KEY=your-secret-key DEBUG=True DATABASE_URL=sqlite:///db.sqlite3 5. Run Migrations bash python manage.py migrate 6. Start the Development Server bash python manage.py runserver 7. Obtain JWT Tokens Use the /api/token/ endpoint to get access and refresh tokens for authentication.

API Endpoints Authentication Method Endpoint Description POST /api/token/ Obtain JWT access and refresh tokens. POST /api/token/refresh/ Refresh an expired access token. User Management Method Endpoint Description POST /api/users/ Create a new user. GET /api/users// Get user details by ID. PUT /api/users// Update user details. DELETE /api/users// Delete a user. Recipe Management Method Endpoint Description POST /api/recipes/ Create a new recipe. GET /api/recipes/ Get a list of all recipes (with pagination). GET /api/recipes// Get details of a specific recipe. PUT /api/recipes// Update a recipe. DELETE /api/recipes// Delete a recipe. Search and Filters Method Endpoint Description GET /api/recipes/?category= Filter recipes by category. GET /api/recipes/?ingredient= Filter recipes by ingredient. GET /api/recipes/?search= Search recipes by title, category, or ingredients. Main Methods and Functions Authentication TokenObtainPairView: Provides endpoints to generate JWT tokens. IsAuthenticated: Ensures only logged-in users can access certain endpoints. User Management UserSerializer: Validates and serializes user data. UserViewSet: Handles CRUD operations for users. Recipe Management RecipeSerializer: Validates and serializes recipe data. RecipeViewSet: Handles CRUD operations for recipes. create(): Creates a new recipe associated with the authenticated user. update(): Updates a recipe; only the owner can modify. destroy(): Deletes a recipe; only the owner can delete. Search and Filters SearchFilter: Enables search functionality for recipes. RecipeFilterBackend: Custom filtering by category and ingredients. Pagination PageNumberPagination: Paginates the recipes to handle large datasets efficiently.

Deployment: Install Heroku CLI:

bash heroku login Create a Heroku app:

bash heroku create Push to Heroku:

bash git push heroku main Run migrations:

bash heroku run python manage.py migrate Contributing Fork the repository. Create a feature branch: git checkout -b feature-name. Commit changes: git commit -m "Add feature". Push to the branch: git push origin feature-name. Submit a pull request.

License: This project is licensed under the MIT License.
