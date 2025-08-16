# Listings App

The **Listings App** is a central part of the alx_travel_app project designed to manage AirBnB-like property listings, customer bookings, and reviews. This app provides data models and serializers that form the foundation of a property booking system.

## Features

- List and manage properties available for rent.
- Track booking details and status for each property.
- Collect user reviews with rating validation.
- Ensure data consistency with constraints and relationships.

---

## Models

### 1. Listing

Represents a rental property with fields like name, description, location, and price.

**Fields:**
- `property_id`: Unique ID (UUID, Primary Key)
- `name`: Property name (Required)
- `description`: Property description (Required)
- `location`: Address or geographical info (Required)
- `price_per_night`: Price in currency format (Required)
- `created_at`: Timestamp when the listing was created
- `updated_at`: Timestamp when the listing was last updated

**Relationships:**
- One-to-One with `Booking`
- One-to-Many with `Review`

---

### 2. Booking

Captures booking information associated with a listing.

**Fields:**
- `booking_id`: Unique ID (UUID, Primary Key)
- `listing`: Linked to one `Listing` (One-to-One)
- `start_date`, `end_date`: Booking period (datetime)
- `total_price`: Computed or set total for the stay
- `status`: Enum (choices: `Pending`, `Confirmed`, `Canceled`)
- `created_at`: Timestamp when booking was made

---

### 3. Review

Allows users to rate and leave comments on listings.

**Fields:**
- `review_id`: Unique ID (UUID, Primary Key)
- `listing`: Linked to one `Listing` (ForeignKey)
- `rating`: Integer (1 to 5, enforced via `CheckConstraint`)
- `comment`: User’s feedback
- `created_at`: Timestamp of submission

**Validation:**
- Ratings must be between 1 and 5 (`CheckConstraint`)

---

## Serializers

### ListingSerializer

Used to serialize and deserialize `Listing` model data.

**Meta options:**
- `fields = '__all__'`
- `read_only_fields`: `created_at`, `updated_at`, `listing_id`

---

### BookingSerializer

Serializes the `Booking` model. It nests the `ListingSerializer` as read-only.

**Meta options:**
- `fields = '__all__'`
- `read_only_fields`: `created_at`, `booking_id`

---

## Usage

Integrate the models and serializers in your Django views or viewsets to create a full-featured listings API.

### Example:
- Create a property listing
- Book that property
- Add a review

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework

Make sure to add `listings` to `INSTALLED_APPS` in your project’s `settings.py`.

---

## Notes

- UUIDs are used for better uniqueness and security in IDs.
- Booking is a one-to-one relationship to ensure one booking per listing at a time.
- Timezone-aware datetimes are expected if `USE_TZ = True` in `settings.py`.

📦 API Views: ListingView and BookingView
In this project, we've created two API views using Django REST Framework's ModelViewSet to manage the Listing and Booking models.

ModelViewSet is a high-level class provided by DRF that automatically provides implementations for all the standard CRUD operations (Create, Retrieve, Update, Delete, and List). This saves time and avoids writing repetitive boilerplate code.
### These are the endpoints

- GET /listings/ → List all listings

- POST /listings/ → Create a new listing

- GET /listings/<id>/ → Retrieve a specific listing

- PUT /listings/<id>/ → Update a listing

- DELETE /listings/<id>/ → Delete a listing

