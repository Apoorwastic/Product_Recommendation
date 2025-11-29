# Product_Recommendation

## Overview
**Product_Recommendation** is an interactive web dashboard that generates **personalized product recommendations** and **active offers** for users. Users can upload datasets in CSV format, view recommended products for each customer, see current active offers, and export the recommendations as a CSV file. This tool is ideal for marketing teams, e-commerce platforms, or retailers to make data-driven promotional decisions.

---

## Who Can Use It
- **E-commerce Managers:** Quickly identify product suggestions for each customer.  
- **Marketing Teams:** Evaluate active offers and promotions per customer.  
- **Data Analysts:** Generate and export reports in CSV for further analysis.  
- **Retailers:** Understand user preferences and improve engagement.  

---

## Advantages
- **Personalized Recommendations:** Shows tailored products per user for better conversions.  
- **CSV Upload & Export:** Easy import of data and export of recommendations for reporting.  
- **Responsive Dashboard:** Works on desktop and mobile devices.  
- **Visual Clarity:** Product cards, badges, and offer chips make the interface intuitive.  
- **Fast Implementation:** Only requires CSV files; no complex database setup is mandatory.  

---

## How It Works

### 1. Upload CSVs
Users upload five CSV files:  
- `Customers.csv` – Contains customer information (name, ID, etc.)  
- `Products.csv` – Product details including price, name, and images  
- `Purchases.csv` – Tracks historical purchases per user  
- `Reviews.csv` – Contains product reviews and ratings  
- `Offers.csv` – Active promotions  

All CSV uploads happen in a single row using a clean, centered upload panel.  

---

### 2. Generate Recommendations
- The dashboard fetches each customer’s data and generates **personalized product recommendations**.  
- Recommended products include discount badges, images, and names.  
- Active offers are displayed using chips for visual clarity.  

---

### 3. Export CSV
- Users can download a CSV file containing the exact recommendations and offers displayed in the dashboard.  
- The CSV export ensures **easy reporting** and offline analysis.  

---

## Tech Stack

| Layer | Technology/Concept |
|-------|------------------|
| **Frontend** | HTML, CSS, JavaScript, Flexbox & Grid, Responsive Design |
| **Backend** | Python (FastAPI / Flask), REST APIs |
| **Data Handling** | CSV parsing, JSON APIs |
| **UI Components** | Product cards, badges, offer chips, upload buttons |
| **Version Control** | Git & GitHub |
| **Deployment** | Localhost or cloud server (optional) |
| **Extras** | Fallback images for missing product images |

---

## Concepts Used
1. **HTML & CSS**: Structure, layout, and responsive design using Flexbox/Grid.  
2. **JavaScript**: Fetching APIs, dynamic DOM manipulation, generating product cards, and handling file uploads.  
3. **CSV Handling**: Uploading, parsing, and generating CSV files for download.  
4. **REST API Integration**: Fetching users, recommendations, and offers from backend endpoints.  
5. **Frontend Components**: Cards for products, badges for discounts, and chips for offers.  
6. **Responsive Layout**: Two users per row on large screens, single column on smaller screens.  
7. **Fallback Images**: Display default images if product images are missing.  

---

## Dashboard Layout

### 1. Upload Section
- All CSV files are uploaded in a single row.  
- Upload button triggers backend data processing.  

### 2. Recommendations & Offers Section
- Displays user cards in **two columns per row**.  
- Each card shows:  
  - User name and ID  
  - Recommended products with discount badges  
  - Active offers with chips  

### 3. CSV Export Button
- Positioned above the Recommendations & Offers heading for quick download.  

---

## Screenshots
You can add screenshots using Markdown like this:
<img width="1918" height="995" alt="home" src="https://github.com/user-attachments/assets/01a5af06-4dc5-449c-b3bb-d49ce214ae5d" />
<img width="1918" height="992" alt="uploading" src="https://github.com/user-attachments/assets/a7681dcb-f4f9-4ea3-a371-81d7b7c0e8a3" />
<img width="1918" height="997" alt="list1" src="https://github.com/user-attachments/assets/c441434d-f5a0-4ca9-a837-c8a0bbff702a" />

<img width="1918" height="1001" alt="list2" src="https://github.com/user-attachments/assets/0cbe0498-7121-424a-ba21-1b7dbbde6025" />

---

## Quick Start

1. **Clone the repository**  

git clone https://github.com/Apoorwastic/Product_Recommendation.git
cd Product_Recommendation
Run a local server

Using Python 3:

bash
Copy code
python -m http.server 8000
Using Node.js:

bash
Copy code
npm install -g http-server
http-server -p 8000
Open the dashboard
Go to http://localhost:8000 in your browser.

Upload CSV files
Upload Customers.csv, Products.csv, Purchases.csv, Reviews.csv, and Offers.csv, then click Upload All.

View recommendations & offers
Users are displayed two per row with recommended products and active offers.

Export CSV
Click Export CSV to download all recommendations and offers.
