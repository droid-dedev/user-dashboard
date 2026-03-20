# User Dashboard

## Description
A web-based user dashboard application that provides a simple and intuitive interface for managing user data and interactions. The dashboard allows users to view and update their profile information, track their activities, and engage with other users.

## Features

### Core Features

* User Profile Management: View and update personal information, including profile picture, bio, and contact details.
* Activity Tracking: View a list of activities, including login history, posts, and comments.
* User Interaction: Send and receive private messages with other users.
* Notifications: Receive notifications for new messages, friend requests, and activity updates.

### Additional Features

* Customizable Dashboard: Users can personalize their dashboard with their preferred layout and settings.
* Search Functionality: Search for other users, groups, or activities.
* Groups Management: Create and manage private groups for discussion and collaboration.

## Technologies Used

* Frontend: React.js, Redux, CSS (SCSS)
* Backend: Node.js, Express.js, MongoDB
* Database: MongoDB
* API: RESTful API for data exchange

## Installation

### Prerequisites

* Node.js (>= 14.17.0)
* MongoDB (>= 4.2.3)
* Yarn (>= 1.22.10)

### Installation Steps

1. Clone the repository using `git clone https://github.com/your-username/user-dashboard.git`.
2. Install the dependencies by running `yarn install` in the project root.
3. Start the application by running `yarn start`.
4. Configure the MongoDB connection by creating a `.env` file in the root directory with the following content:
```makefile
MONGO_URI=mongodb://localhost:27017/user-dashboard
```
5. Run the application by executing `yarn start`.

## Running the Application

The application will start on port 3000 by default. Access the dashboard at `http://localhost:3000` in your web browser.

## Contributing

Contributions are welcome and encouraged. Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. For more information, please refer to the [License File](LICENSE).