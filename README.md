# To Do List Project

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone git@github.com:SaugatMgr/To-Do-List.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd To-Do-List
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Migrate changes**
   - Run the following command to migrate changes to database:
      ```bash
      python manage.py migrate
      ```
2. **Create a superuser:**
    - Run the following command and follow the prompts:
        ```bash
        python manage.py createsuperuser
        ```
        This is for accessing admin panel and performing administrative works as well as access the stored records in the database

3. **Run the server:**
    ```bash
    python manage.py runserver
    ```
