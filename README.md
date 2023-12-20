
# Customer Notifications

This Notification projetct provides a flexible service for sending notifications to users through various channels. Built with Python, it offers a scalable architecture that allows for easy integration into existing applications. The service supports different notification types, including web, email, and mobile push notifications, enabling seamless communication with users across multiple channels.


# Key Features

- Multi-channel Support: Send notifications through web, email, or mobile push channels.

- Scheduled Notifications: Schedule notifications for future delivery based on user preferences.

- Customizable Templates: Utilize customizable templates for different notification types.

- Error Handling: Robust error handling with customizable exception classes for handling different scenarios.

- Test Coverage: Comprehensive test suite ensuring reliability and stability.

# Project 

<img width="856" alt="image" src="https://github.com/Luiz-Cruz/customer-notifications/assets/54514011/9975e7a7-7432-42e5-8f85-6a74e55028f1">




# Prerequisites
- Python 3.10 or higher
- Poetry (dependency management)

# Installation

1. Clone the repository:

```bash
$ https://github.com/Luiz-Cruz/customer-notifications.git
```


2. Start and await the containers to build up
   
```bash
$ docker-compose up --build
```

# HTTP Collection

   https://documenter.getpostman.com/view/15447501/2s9Ykq6fVX


# RabbitMQ:
```bash
localhost:15672
```

#  MongoDB:
```bash
localhost:8081
```

## Env

- base_users: admin
- base_passwords: admin

# Tests 

Be sure to be in the main directory, then run:

``` bash
$ coverage run -m pytest
$ coverage report -m
```
```
