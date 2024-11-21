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
4. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

5. **Activate the virtual environment:**

    On Windows:

    ```bash
    .\.venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source .venv/bin/activate
    ```
6. **Set up environment variables:**

    Create a `.env` file in the project root directory and add the following variables:

    ```
    DEBUG=True
    SECRET_KEY=your_secret_key_here
    ALLOWED_HOSTS="*"
    ```
    For Simplicity, you can just keep SECRET_KEY="my-secret-key"

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
4. **Access the Site**
    ```
    127.0.0.1:8000
    ```
    Go to this url in the browser
