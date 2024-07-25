# Book Review Website

Welcome to the Book Review Website! This Django-based project allows users to register, log in, and submit reviews for their favorite books. Each book has a dedicated page displaying its title, author, cover image, and insightful reviews.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User Registration and Authentication
- Add and Edit Book Reviews
- Star Rating System
- Responsive Design
- User Profile with Personal Reviews

## Screenshots

### Home Page
![homepage1](https://github.com/user-attachments/assets/0d96c00d-8336-4edf-ac55-0cf3dc1da129)
![homepage2](https://github.com/user-attachments/assets/f373fcef-3a15-47d6-8bf7-d2b2d61caed9)

### Book Details Page
![bookdetailspage](https://github.com/user-attachments/assets/993c1e4a-4537-4e70-a3d6-9d0e00eaebec)
![bookdetailspage1](https://github.com/user-attachments/assets/776b9245-833e-4bca-80a7-5806f203d32b)

### Add a Review
![addreviewpage](https://github.com/user-attachments/assets/ec4fe8ac-1eb8-4406-9835-2b9154e39910)

### Login Page
![loginpage](https://github.com/user-attachments/assets/e011d9de-68f8-4c46-9693-26787be05ba7)

### Register Page
![registerpage](https://github.com/user-attachments/assets/37612aa3-6042-4e9d-aa7d-50f6ba390097)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harshit433/Book-review-website.git
   cd book-review-website
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the website.

## Usage

- **Register**: Create a new account to access personalized features.
- **Login**: Log in to your account to add or edit your reviews.
- **Add a Review**: Navigate to a book's detail page and submit your review with a star rating.
- **User Profile**: View and manage your reviews on your profile page.

## Technologies

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite (default for Django)

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to:

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [your-username](https://github.com/your-username)

---

Replace the placeholder text (like `your-username`, `your-email@example.com`, etc.) with your actual details. Also, make sure the paths to the screenshots are correct. If you have any additional features or instructions, feel free to add them to the relevant sections.
