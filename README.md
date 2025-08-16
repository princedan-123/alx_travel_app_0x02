
# **Chapa API Payment Integration** 💳

This project, **Milestone 4: Payment Integration with Chapa API**, focuses on integrating the Chapa Payment Gateway into a Django-based travel booking application. The main goal is to implement a secure and reliable payment workflow, from initiation to verification, while ensuring a smooth user experience. This README provides an overview of the project, key features, setup instructions, and the learning outcomes achieved.

<hr>

## **Overview**

This project involved integrating the **Chapa API** into a Django travel booking application. We created a secure payment flow that allows users to pay for their bookings and receive automated confirmations. The workflow includes initiating payments, securely handling API credentials, tracking transaction status, and sending background email notifications using **Celery**. The project uses a **PostgreSQL** database to store booking and payment data.

<hr>

## **Key Features**

-   **Secure Credential Management**: API keys are stored in environment variables using **`dotenv`**, ensuring they are not exposed in the codebase.
    
-   **Payment Model**: A **`Payment`** model was created in `listings/models.py` to track transaction details, including the transaction ID, booking reference, amount, and payment status.
    
-   **API Endpoints**:
    
    -   An endpoint in `listings/views.py` initiates a payment by making a POST request to the Chapa API.
        
    -   A separate endpoint verifies the payment status with Chapa, updating the `Payment` model accordingly.
        
-   **Robust Payment Workflow**: The system directs users to the Chapa payment page, verifies the payment status upon completion, and handles both successful and failed transactions gracefully.
    
-   **Asynchronous Email Notifications**: **Celery** is used to send automated booking confirmation emails in the background after a successful payment, preventing delays in the user's experience.
    

<hr>

## **Technical Implementation**

### **Setting up Chapa API**

1.  **Account Creation**: An account was created on the Chapa developer portal to obtain the API keys.
    
2.  **Environment Variables**: The secret key was stored in the `.env` file as `CHAPA_SECRET_KEY` and accessed securely within the Django application.
    

### **Payment Model (`listings/models.py`)**

A `Payment` model was created to store payment-related information. It includes fields for the booking, transaction ID, payment status (e.g., 'Pending', 'Completed', 'Failed'), and amount. This model serves as the single source of truth for all payment transactions.

### **Payment API View (`listings/views.py`)**

-   **Payment Initiation**: A **`POST`** request is made to the Chapa API using the **`requests`** library. The request includes the booking amount and user details.
    
-   **Transaction Tracking**: The transaction ID returned by Chapa is saved in the `Payment` model, with the initial status set to **`'Pending'`**.
    
-   **Payment Verification**: A separate endpoint handles the verification of the payment by querying the Chapa API. The `Payment` model is updated based on the API's response, setting the status to **`'Completed'`** or **`'Failed'`**.
    

### **Testing**

The entire payment flow was tested using Chapa's **sandbox environment**. This ensured that payment initiation, redirection, verification, and status updates functioned as expected before deploying to a live environment. **Screenshots** and logs were included to demonstrate successful transactions and accurate status updates in the database.

<hr>

## **Learning Outcomes**

This project provided hands-on experience with:

-   Integrating a third-party payment gateway into a **Django** application.
    
-   Implementing **secure credential management**.
    
-   Designing and implementing **Django models** for transactional data.
    
-   Using **HTTP requests** to communicate with external APIs.
    
-   Implementing **asynchronous background tasks** with **Celery** for improved performance.
    
-   Developing robust **error handling** for payment failures.
    

This project simulates a **real-world use case**, providing essential skills for backend development in e-commerce and fintech.