# Accounts App

This Django app provides user authentication functionality for the Prime Times news application.

## Features

- **User Registration**: Users can create new accounts with username, email, and password
- **User Login**: Secure authentication with username/email and password
- **User Logout**: Secure logout functionality
- **User Profile**: View user information and account details
- **Login Required Protection**: Certain views require authentication

## URLs

- `/login/` - User login page
- `/signup/` - User registration page
- `/logout/` - User logout (redirects to login)
- `/profile/` - User profile page (requires authentication)

## Views

- `login_page()` - Handles user login
- `signup_page()` - Handles user registration
- `logout_view()` - Handles user logout (requires authentication)
- `profile_view()` - Shows user profile (requires authentication)

## Forms

- `CustomUserCreationForm` - User registration form with validation
- `CustomAuthenticationForm` - User login form

## Authentication Requirements

The following views require user authentication:
- News creation (`/create/`)
- News editing (`/edit/<id>/`)
- User profile (`/profile/`)
- User logout (`/logout/`)

## Usage

1. **Registration**: Users visit `/signup/` to create new accounts
2. **Login**: Users visit `/login/` to authenticate
3. **Protected Views**: Authenticated users can access news creation/editing
4. **Profile**: Users can view their account information at `/profile/`
5. **Logout**: Users can log out from the profile page or navigation menu

## Security Features

- CSRF protection on all forms
- Password validation using Django's built-in validators
- Secure session management
- Login required decorators on sensitive views
- Automatic redirect to login for unauthenticated users

## Templates

- `login.html` - Login form with error handling
- `signup.html` - Registration form with validation
- `profile.html` - User profile display
- All templates extend `base.html` and include proper styling

## Dependencies

- Django 5.2+
- Django's built-in authentication system
- Tailwind CSS for styling
