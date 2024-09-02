# API
This is intended to practice, it´s developed with FastAPI library to get use to it and learn how to do it. Also this will be connected with GUI project in order to manage and make the requets easier. The API is focus to consume vehicle data.

## Supported Endpoints 
- PUT -> AddCar: It's available to send and create a new vehicle register into DB.
- GET -> GetAllCars: It brings all records stored in DB.
- GET -> GetSpecificCar: It brings a specific record from DB it requires an ID.

## Comming up Endpoints
- GET -> GetChanges: It brings all records in Chnages table.
- GET -> GetSpecificChange: It brings an specific record using changeId or/and timestamp.

## TODO
- Add user table to DB.
- Add changes table to DB.
- Add Timestamp, ID, UserID into changes table.
- Add UserID, Name, Position into user table.
- Add Endpoint to get all the changes registered into Car table and append the record to Changes table also with a timestamp.
- Add Endpoint to get a record from Changes table using the timestamp and also using an specific ID.
