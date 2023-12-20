
# Customer Notifications

This Notification projetct provides a flexible service for sending notifications to users through various channels. Built with Python, it offers a scalable architecture that allows for easy integration into existing applications. The service supports different notification types, including web, email, and mobile push notifications, enabling seamless communication with users across multiple channels.


# Key Features

- Multi-channel Support: Send notifications through web, email, or mobile push channels.

- Scheduled Notifications: Schedule notifications for future delivery based on user preferences.

- Customizable Templates: Utilize customizable templates for different notification types.

- Error Handling: Robust error handling with customizable exception classes for handling different scenarios.

- Test Coverage: Comprehensive test suite ensuring reliability and stability.

# Project scope

![image](https://github.com/Luiz-Cruz/customer-notifications/assets/54514011/ba808749-6dd8-466f-ac68-46f01f2d12b1)



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

3. Get the collection

   https://documenter.getpostman.com/view/15447501/2s9Ykq6fVX


4. RabbitMQ:
```bash
localhost:15672
```

5. MongoDB:
```bash
localhost:8081
```

## Env

- base_users: admin
- base_passwords: admin
