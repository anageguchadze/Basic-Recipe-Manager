# Django Recipe Application

This project is a simple recipe management web application built using Django. It allows users to create, view, edit, and delete recipes. Each recipe includes a name, list of ingredients, and instructions.

## Features

- **View All Recipes**: Display a list of all the recipes saved in the system.
- **Recipe Details**: View the details of a specific recipe, including ingredients and instructions.
- **Add Recipe**: Add new recipes by providing the name, ingredients, and instructions.
- **Edit Recipe**: Update the name, ingredients, or instructions of an existing recipe.
- **Delete Recipe**: Remove a recipe from the system.

## Models

1. **Recipe**
   - `name`: The name of the recipe (maximum 100 characters).
   - `ingredients`: A text field to list the ingredients required for the recipe.
   - `instructions`: A text field to describe the steps involved in preparing the recipe.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Basic-Recipe-Manager
