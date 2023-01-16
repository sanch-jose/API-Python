# API-Python

This project consist of a REST API that reflects how a social app works. It simulates a post system, where users can share their message (title + content) and upvote the content they like.

The API has been developed using Python, FastAPI and a PostgreSQL Database. During the development I´ve been using Postman and Pgadmin4 to test the different implementations while developing.
Finally, I developed tests for the code using Pytest, implemented Docker for the deployment and Github Actions to have a pipeline for CI/CD.

## Features & Tools

 Here you will find a summary of some of the features and tools used for the development not mentioned before:
 
- Uvicorn
- SQLAlchemy models
- ORM
- Pydantic
- Alembic migrations
- CORS (Cross Origin Resource Sharing)
- Oauth2
- JWT token authentication
