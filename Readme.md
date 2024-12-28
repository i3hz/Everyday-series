

# GeminiHashtagGenerator

## Project Description
The `GeminiHashtagGenerator` is a Python-based tool that uses Google's Gemini API to generate relevant and optimized hashtags for social media posts. It can create up to 10 relevant hashtags for a given post, considering both popular and niche tags. The tool also suggests relevant categories (e.g., food, travel, fitness) based on the content of the post. This is helpful for individuals or businesses looking to enhance their social media visibility by using the right hashtags.

## Setup Instructions

### Prerequisites
- Python 3.7+ installed on your machine.
- A Google Gemini API key (you need to obtain this from Google).

### Steps to Set Up
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/GeminiHashtagGenerator.git
   cd GeminiHashtagGenerator
   ```

2. **Install Required Dependencies:**
   Create a virtual environment (optional but recommended) and install the necessary dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install google-generativeai
   ```

3. **Set Up API Key:**
   - Obtain your Google Gemini API key.
   - Create a file named `key.py` in the root directory and store your key like this:
     ```python
     key = 'YOUR_API_KEY'
     ```

4. **Run the Application:**
   You can now run the main program to start generating hashtags for your posts.
   ```bash
   python main.py
   ```

### Example Usage:
- When prompted, enter the content of your social media post. The program will suggest relevant categories and generate hashtags for your post.

## Features Overview
- **Hashtag Generation:** Generates up to 10 relevant hashtags based on a given social media post.
- **Category Suggestions:** Suggests categories like food, travel, fitness, etc., based on the content of the post.
- **Customization:** The tool allows you to filter hashtags based on a specific category for better relevance.
- **Error Handling:** If the tool encounters any issues, it will print an error message and continue running.
- **Async Operations:** The program uses asynchronous functions to fetch results from the Gemini API efficiently.

## License
This project is licensed under the MIT License.
```
