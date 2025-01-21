# GamingVsGambling

## Overview
GamingVsGambling is a FastAPI-based application that classifies apps as either gaming or gambling based on their description, permissions, and user reviews from the Google Play Store. It uses Google Generative AI to analyze and extract important information from the app data.

## Features
- Fetch app details from the Google Play Store.
- Analyze app descriptions, permissions, and reviews.
- Classify apps as gaming or gambling with detailed explanations.

## Setup

### Prerequisites
- Python 3.8+
- Google Generative AI API Key
- Google Play Scraper

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/GamingVsGambling.git
    cd GamingVsGambling
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add your Google Generative AI API Key:
        ```
        GEMINI_API_KEY=your_api_key_here
        ```

## Usage

### Running the Application
1. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. Access the API at `http://127.0.0.1:8000`.

### API Endpoint
- **GET /classify**: Classify an app as gaming or gambling.
    - **Parameters**:
        - `game_name` (str): The name of the app to classify.
    - **Response**:
        - `result` (json): The classification result with explanations.

### Example Request
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/classify?game_name=example_game' \
  -H 'accept: application/json'
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License.