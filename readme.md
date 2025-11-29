Brand Marketing Recommendation Dashboard

A Complete AI-Driven Product Recommendation & Offer Personalization System

📌 Overview

The Brand Marketing Recommendation Dashboard is an AI-powered tool designed for marketers, e-commerce teams, CRM analysts, and data strategists who want to generate personalized product recommendations and promotional offers for customers based on:

Purchase history

Product catalog

User reviews

Active marketing offers

The tool reads CSV files uploaded by the user and automatically generates:

🎯 Top product recommendations for each customer

🎁 Best matching offers

📊 A clean UI to visualize everything

📤 One-click exportable CSV for marketing campaigns

This system is ideal for businesses wanting a plug-and-play recommendation engine without needing complex AI infrastructure.

👥 Who Can Use This Tool?

This dashboard is designed for:

✔ Marketing Teams

To run personalized campaigns, retargeting, and email marketing.

✔ E-Commerce Businesses

To recommend products similar to Amazon’s “Customers Also Bought”.

✔ CRM / Loyalty Teams

To maximize customer engagement using tailored promotions.

✔ Data Analysts

To create customer insights without coding.

✔ Students / Hackathon Participants

Who want a complete working ML system for product recommendations.

🚀 Key Advantages
✅ 1. No Coding Needed

Upload CSV files → get recommendations instantly.

✅ 2. Works With Any Dataset

Plug your own customers, products, reviews, and offers.

✅ 3. Fully Offline

No internet dependency — everything runs locally.

✅ 4. Real-Time Recommendations

Each customer gets suggestions in milliseconds.

✅ 5. Auto Indexing

Products are automatically indexed for semantic search.

✅ 6. AI-Powered Matching

Uses text embeddings to recommend based on:

Product similarity

Review sentiment

Purchase history

Offer compatibility

✅ 7. Exportable CSV

Perfect for email, SMS, WhatsApp, and ad campaigns.

✅ 8. Clean, Modern UI

Shows:

Customer name

Product cards with images

Discounts

Matching offers

Two customers per row for readability

⚙️ How It Works

The system follows a 5-stage pipeline:

1️⃣ Upload CSV Files

The tool accepts:

Type	Purpose
Customers.csv	Basic customer data
Products.csv	Catalog: names, categories, prices, images
Purchases.csv	User purchase history
Reviews.csv	Product review sentiment
Offers.csv	Active discount campaigns

All files are uploaded in one row in the UI using the Upload All button.

2️⃣ Automatic Product Indexing

After upload:

Product descriptions

Names

Categories

…are converted into semantic vectors using embeddings.

This enables AI to detect similarity between:

Products

Categories

User interests

3️⃣ Recommendation Engine

For each customer, the engine evaluates:

✔ Past purchases
✔ Similar product embeddings
✔ Category affinity
✔ Review sentiment
✔ Price & discount preferences

The output:

Top 5 recommended products

Best matching active offers

4️⃣ UI Display

Results are shown in a 2-column grid:

Product images

Discount badges

Offer chips

Customer name + ID

Everything is centered beautifully.

5️⃣ Export as CSV

A single click downloads:

recommendations.csv


This file includes:

Customer ID

Recommended product names

Active offers

All discounts

Perfect for marketing uploads.

🛠️ Installation & Running the App
1. Install dependencies
pip install -r requirements.txt

2. Start the FastAPI backend
uvicorn main:app --reload

3. Open the Dashboard

Open the HTML file in any browser:

dashboard.html


You’re ready to go!

🔌 API Endpoints
Method	Endpoint	Purpose
POST	/upload/customers	Upload customers CSV
POST	/upload/products	Upload products CSV
POST	/upload/purchases	Upload purchases CSV
POST	/upload/reviews	Upload reviews CSV
POST	/upload/offers	Upload offers CSV
GET	/users	List all customers
GET	/recommend/{user_id}	Get recommendations
GET	/export_csv/	Download full recommendations CSV

All endpoints return clean JSON.

🗂️ CSV Format Guide
Products CSV
product_id,name,category,price,discount,image
P101,Blue Denim Jeans,Clothing,1599,20,https://img...
P102,Black Hoodie,Clothing,1299,15,https://img...

Customers CSV
id,name,age,city
C001,Amit Sharma,28,Delhi
C002,Neha Kapoor,24,Mumbai

Purchases CSV
customer_id,product_id
C001,P101
C002,P105

Reviews CSV
product_id,review_text,rating
P101,"Good quality",5

Offers CSV
offer_id,title,discount,category
O01,Handbag Fest,20,Bags

🖼️ Screenshots

(Add your screenshots here)

/screenshots/dashboard.png
/screenshots/recommendations.png
/screenshots/upload.png

📄 License

This project is free to use for educational and commercial purposes.
Credit not required but always appreciated 😊.