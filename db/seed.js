db = db.getSiblingDB('cronos');

db.createCollection('users');
db.createCollection('notifications');
db.users.createIndex({ email: 1 }, { unique: true });


db.users.insertMany([
    {
        "_id": "e2b3b6d8-4d53-4a81-a64a-8f20a9d8d1aa",
        "email": "jsmith@gmail.com",
        "opt_out": false
    },
    {
        "_id": "f1a2c8e7-6b84-4c7f-93c5-9d8e2b1a3f4d",
        "email": "janedoe@yahoo.com",
        "opt_out": false
    },
    {
        "_id": "d9c8b7a6-5f4e-4d3c-8b2a-1e9d0c3b4a5f",
        "email": "mike_jones@hotmail.com",
        "opt_out": false
    },
    {
        "_id": "a1b2c3d4-e5f6-4a9b-8c7d-1e2f3a4b5c6d",
        "email": "emma.smith@outlook.com",
        "opt_out": true
    },
    {
        "_id": "b1a2c3d4-e5f6-4a9b-8c7d-1e2f3a4b5c6e",
        "email": "alexander_t@icloud.com",
        "opt_out": false
    },
    {
        "_id": "c1b2a3d4-e5f6-4a9b-8c7d-1e2f3a4b5c6f",
        "email": "laurabrown@live.com",
        "opt_out": true
    },
    {
        "_id": "d1e2f3a4-b5c6-4d9a-8b7c-1e2f3a4b5c6g",
        "email": "samwilliams@protonmail.com",
        "opt_out": false
    },
    {
        "_id": "e1d2c3b4-a5f6-4d9a-8b7c-1e2f3a4b5c6h",
        "email": "olivia_jones@yandex.com",
        "opt_out": false
    },
    {
        "_id": "f1e2d3c4-b5a6-4d9a-8b7c-1e2f3a4b5c6i",
        "email": "chris.miller@uol.com",
        "opt_out": true
    },
    {
        "_id": "a1b2c3d4-e5f6-4d9a-8b7c-1e2f3a4b5c6j",
        "email": "emily_white@inbox.com",
        "opt_out": false
    },
    {
        "_id": "b1c2d3e4-f5a6-4d9a-8b7c-1e2f3a4b5c6k",
        "email": "davidbrown@zoho.com",
        "opt_out": false
    },
    {
        "_id": "c1b2a3d4-e5f6-4d9a-8b7c-1e2f3a4b5c6l",
        "email": "sarah.garcia@protonmail.com",
        "opt_out": true
    },
    {
        "_id": "d1e2f3a4-b5c6-4d9a-8b7c-1e2f3a4b5c6m",
        "email": "jonathansmith@icloud.com",
        "opt_out": false
    },
    {
        "_id": "e1d2c3b4-a5f6-4d9a-8b7c-1e2f3a4b5c6n",
        "email": "isabella.green@yahoo.com",
        "opt_out": false
    },
    {
        "_id": "f1e2d3c4-b5a6-4d9a-8b7c-1e2f3a4b5c6o",
        "email": "michaeljohnson@outlook.com",
        "opt_out": true
    },
    {
        "_id": "a1b2c3d4-e5f6-4d9a-8b7c-1e2f3a4b5c6p",
        "email": "sophia_wilson@gmail.com",
        "opt_out": false
    },
    {
        "_id": "b1c2d3e4-f5a6-4d9a-8b7c-1e2f3a4b5c6q",
        "email": "lucasanderson@hotmail.com",
        "opt_out": false
    },
    {
        "_id": "c1b2a3d4-e5f6-4d9a-8b7c-1e2f3a4b5c6r",
        "email": "madison_carter@live.com",
        "opt_out": true
    },
    {
        "_id": "d1e2f3a4-b5c6-4d9a-8b7c-1e2f3a4b5c6s",
        "email": "nathanthompson@yandex.com",
        "opt_out": false
    },
    {
        "_id": "e1d2c3b4-a5f6-4d9a-8b7c-1e2f3a4b5c6t",
        "email": "ava_harris@aol.com",
        "opt_out": false
    },
    {
        "_id": "f1e2d3c4-b5a6-4d9a-8b7c-1e2f3a4b5c6u",
        "email": "jacobwilson@inbox.com",
        "opt_out": true
    }
]);
