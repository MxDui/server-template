# Django Custom User Project

This project demonstrates how to implement a custom user model in Django that uses an email address as the primary means of authentication.

## Features

- Custom user model with email authentication
- Extended user attributes like `first_name` and `last_name`
- Custom user manager with helper methods for creating users and superusers
- Integration with Django admin

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone [YOUR REPOSITORY LINK HERE]
   cd [YOUR PROJECT NAME HERE]
   ```

2. **Setup Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Creating a Superuser

To create a superuser for accessing the Django admin interface, run:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter an email address and password.

### Accessing Admin Interface

Once you've created a superuser, you can access the Django admin interface at:

```
http://localhost:8000/admin/
```

Log in using the email and password you set for the superuser.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

This README is a basic template and can be further customized to include more details, such as:

- Project screenshots or GIFs
- A more detailed description of the project
- Details about the tech stack used
- Deployment instructions
- Testing instructions
- Credits and acknowledgements

Remember to replace placeholders like `[YOUR REPOSITORY LINK HERE]` with actual information relevant to your project.
