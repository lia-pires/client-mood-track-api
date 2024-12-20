# Client Mood Track API

This project is a Flask-based API that classifies customer comments into **positive**, **neutral**, or **negative** sentiment using **OpenAI's ChatGPT**. The API stores the classified comments in a non-relational database (MongoDB) for future analysis and reporting. Additionally, customers receive a confirmation of their evaluation via WhatsApp using **Twilio**.

## Features
- **Sentiment Analysis**: ChatOpenAI's ChatGPT classifies comments as positive, neutral, or negative, with confidence scores and explanations.
- **Non-Relational Database Integration**: Stores classified comments and metadata in a flexible document structure.
- **WhatsApp Confirmation**: After submitting feedback, the customer receives a confirmation of their evaluation via WhatsApp using **Twilio**.

## Technologies Used
- **Flask**: For building the API.
- **OpenAI API**: For sentiment analysis using ChatGPT.
- **MongoDB**: For storing classified comments and metadata.
- **Twilio API**: For sending WhatsApp messages to customers.
- **PyMongo**: For database interaction.

## Prerequisites
...

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/client-mood-track-api.git
   cd client-mood-track-api

.
.
.


//v2