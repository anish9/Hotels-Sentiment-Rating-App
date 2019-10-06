# Sentiment-Rating-App 
simple experimental project for building end-to-end Machine Learning Block

# About App

- simple text classifier was trained using Conv and Recurrent Network on yelp reviews dataset.
- Contains 5 labels to classify (each refers to the rating given)
- we reverse the logic by reading the text and giving it a rating by making text as independent and rating as dependent   variable 
-  The trained "Rating Machine" is deployed using Flask API

## Running demo server and making request using curl
```
python3 api.py
```
### Server starts when above code is executed 
```
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

### send request using below curl command

```
curl --request POST   --url http://localhost:5000/analyzetext   --header 'content-type: application/json'   --data '{
        "message":"Excellent eating experience.. from walking in the door and being greeted by employee, seated and drink order taken, was maybe 5 minutes. Meal was served hot and excellent taste. Server was very friendly and helpful."
}'
```
### Output 

```
"The rating for the hotel based on review - 5"

```
