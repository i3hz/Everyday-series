import google.generativeai as genai
from typing import List
import os
import json
import sys
from key import key
class GeminiHashtagGenerator:
    def __init__(self, api_key: str):
        """
        Initialize the hashtag generator with Gemini API key
        
        Args:
            api_key (str): Google API key for Gemini
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Predefined categories for better context
        self.categories = {
            'food': ['cooking', 'foodie', 'recipe', 'foodphotography', 'homemade'],
            'travel': ['wanderlust', 'travelgram', 'explore', 'adventure', 'vacation'],
            'fitness': ['workout', 'gym', 'health', 'motivation', 'exercise'],
            'technology': ['tech', 'coding', 'programming', 'developer', 'software'],
            'photography': ['photo', 'camera', 'photooftheday', 'photographer', 'pictureoftheday'],
        }

    def _create_prompt(self, content: str, category: str = None) -> str:
        """
        Create a structured prompt for Gemini
        
        Args:
            content (str): The social media post content
            category (str): Optional category for context
            
        Returns:
            str: Formatted prompt
        """
        base_prompt = (
            f"Generate at least 5 relevant hashtags for this social media post: '{content}'\n"
            f"Rules:\n"
            f"1. Return only hashtags without '#' symbol\n"
            f"2. Each hashtag should be lowercase and without spaces\n"
            f"3. Make hashtags specific and relevant\n"
            f"4. Include a mix of popular and niche hashtags\n"
            f"5. Return as a String array\n"
        )
        
        if category and category.lower() in self.categories:
            base_prompt += f"\nContext: This is related to {category}. Consider these relevant hashtags: {', '.join(self.categories[category])}"
        
        return base_prompt

    def _parse_response(self, response: str) -> List[str]:
        """
        Parse Gemini's response into a list of hashtags
        
        Args:
            response (str): Raw response from Gemini
            
        Returns:
            List[str]: List of cleaned hashtags
        """
        try:
            hashtags = json.loads(response)
            if isinstance(hashtags, list):
                return hashtags
            if isinstance(hashtags, dict) and 'hashtags' in hashtags:
                return hashtags['hashtags']
        except json.JSONDecodeError:
            hashtags = []
            for line in response.split('\n'):
                cleaned = line.strip().replace('#', '').lower()
                if cleaned and cleaned.isalnum():
                    hashtags.append(cleaned)
        
        return hashtags

    async def generate_hashtags(self, content: str, category: str = None, max_hashtags: int = 10) -> List[str]:
        """
        Generate hashtags for the given content
        
        Args:
            content (str): The social media post content
            category (str): Optional category for context
            max_hashtags (int): Maximum number of hashtags to generate
            
        Returns:
            List[str]: List of generated hashtags
        """
        prompt = self._create_prompt(content, category)
        
        try:
            response = await self.model.generate_content_async(prompt)
            hashtags = self._parse_response(response.text)
            
            filtered_hashtags = []
            for tag in hashtags[:max_hashtags]:
                clean_tag = ''.join(c for c in tag if c.isalnum()).lower()
                if clean_tag:
                    filtered_hashtags.append(clean_tag)
            
            return filtered_hashtags
            
        except Exception as e:
            print(f"Error generating hashtags: {str(e)}")
            return []

    def get_category_suggestions(self, content: str) -> List[str]:
        """
        Suggest relevant categories based on content
        
        Args:
            content (str): The social media post content
            
        Returns:
            List[str]: List of suggested categories
        """
        matching_categories = []
        content_lower = content.lower()
        
        for category, keywords in self.categories.items():
            if any(keyword in content_lower for keyword in keywords):
                matching_categories.append(category)
        
        return matching_categories

# Main function to interact with the user
async def main():
    api_key = key
    generator = GeminiHashtagGenerator(api_key)
    
    while True:
        content = input("\nEnter your social media post (or type 'exit' to quit): ")
        if content.lower() == 'exit':
            print("Goodbye!")
            sys.exit(0)
            
        
        suggested_categories = generator.get_category_suggestions(content)
        if suggested_categories:
            print(f"Suggested categories: {', '.join(suggested_categories)}")
        
        hashtags = await generator.generate_hashtags(content, max_hashtags=8)
        print(f"Generated hashtags: {' '.join(['#' + tag for tag in hashtags])}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
