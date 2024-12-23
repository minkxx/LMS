# LMS - Library Management System

## Introduction
The Library Management System (LMS) is a comprehensive solution designed to manage and streamline the operations of a library. This system allows librarians to manage books, members, and transactions efficiently. It provides an intuitive interface for both librarians and members to interact with the system.

## Features
- **Book Management**: Add, update, delete, and search for books.
- **Member Management**: Register new members, update member information, and manage member records.
- **Transaction Management**: Issue and return books, track due dates, and manage fines.
- **Search Functionality**: Advanced search options for books and members.
- **Librarian**: Log in to manage books, members, and transactions.

## Setup Instructions
To set up and run the LMS project, follow these steps:

### Prerequisites
- Ensure you have [Python 3.8+](https://www.python.org/downloads/) installed.
- Install [MySQL](https://www.mysql.com/) and ensure it is running.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/minkxx/LMS.git
    cd LMS
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv/Scripts/activate # To activate venv On windows

    source venv/bin/activate  # On Linux/Mac 
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database connection:
    Create a `.env` file in the project root and add your database credentials:
    ```env
    HOST=localhost
    USER=yourusername
    PASSWORD=yourpassword
    DATABASE=lms
    ```

5. Setup the database:
    - Open your mysql workbench and copy the codes of `schema/LMS-Schema.sql` and run it to setup the database.
### Running the Project
1. Run the main script:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to interact with the LMS.

### Note
Ensure that the MySQL server is running and the database credentials in the `.env` file are correct before running the project.

## Acknowledgements

I would like to express my sincere gratitude to my teacher, [Mr. Tarun Kumar Sharma](https://github.com/ownway08), for their invaluable guidance and support throughout this project. Your expertise and encouragement have been instrumental in the successful completion of this Library Management System.

I would also like to thank my teammates, Shrestho Nath, and Papiya R.Das, for their hard work, dedication, and collaboration. This project would not have been possible without your contributions and teamwork.

Thank you all for your support and assistance in making this project a success.

## Contributing
We welcome contributions to improve the LMS. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact us at [aryuokk@gmail.com](mailto:aryuokk@gmail.com).
