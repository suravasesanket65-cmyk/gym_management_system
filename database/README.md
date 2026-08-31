# CORESA Gym Management System - Database Export

## Database Information
- **Database Name:** `gyms`
- **Database Type:** MySQL (Compatible with MariaDB)
- **Engine:** InnoDB
- **Encoding:** UTF-8 / utf8mb4

## How this SQL file was generated
This SQL file was generated using the standard `mysqldump` utility directly from the active production database, ensuring full preservation of the schema, foreign keys, constraints, indexes, and real application data. Duplicate and legacy tables (such as `core_gymmember` and `core_simpletrainer`) were deliberately excluded and removed from the active schema to maintain normalization.

## How to create the database
Before importing, ensure the database exists in your MySQL server. Log into MySQL:

```sql
CREATE DATABASE gyms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## How to import the SQL file
You can import the SQL dump into the empty database using the terminal:

```bash
mysql -u root -p gyms < database/core_sa_database.sql
```
*(You will be prompted to enter your MySQL password)*

## How to configure `.env`
Ensure your Django project root has a `.env` file containing the correct credentials matching the newly imported database:

```env
DB_NAME=gyms
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

## How to run Django migrations after import
The SQL file includes the `django_migrations` table, so Django already knows which migrations have been applied. However, it is good practice to run the check commands to ensure synchronization:

```bash
python manage.py makemigrations --check
python manage.py check
```
There should be no missing migrations.

## How to verify the database
A verification script is provided to automatically inspect the database using Django's database connection.

```bash
python database/verify_database.py
```
This script checks that all expected core application tables exist and that deprecated duplicates have been safely removed.

## Important Security Warnings
- **DO NOT** commit the `.env` file to version control.
- **DO NOT** expose this SQL file publicly if it contains real user data, as it includes hashed passwords, emails, and phone numbers.
- The `auth_user` passwords are encrypted using Django's secure hashing algorithms, but the file must still be protected as sensitive PII.
