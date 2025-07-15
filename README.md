# User-Persona-Builder

Hello Everyone I have built this project which will scrape the posts and comments from the user's Reddit profile page and create a Persona for him/her. The two files present in the repository are the results of my two different approaches to solve this problem. 'kojied.txt' is the file created by running the scraper.py which runs on offline LLM and 'Hungry-Move-6603.txt' is the file created by running the scraper_api.py which uses Gemini's API to run.

I have used two methods for this:

1. Using Ollama's Phi model:
   scraper.py is the python script which runs on offline LLM and in order to run that file you will need to follow these steps:
       a. Install Ollama from its official website and launch it.
       b. Now on your terminal run this command 'ollama pull phi'. I am using phi model because my PC does not have sufficient RAM to run bigger models like Llama2 or mistral, therefore the result may also be compromised a bit.
       c. Now install all the dependencies and libraries that we have imported in our python script.
       d. Create a Reddit App on its official website which help us to use Reddit's API to fetch the comments and posts of a user legally.
       e. Now enter all your Reddit app credentials in the code.
       f. Now choose the target_username that you want to build the persona of.
       g. Once all these steps are done you can run the code and it will create a text file with the persona of the target_username.
   
3. Using Gemini API:
   scraper_api.py is the python script which runs on Gemini's API and in order to run that file follow these steps:
       a. Create an API key of Gemini and store it the .env file by the name 'GOOGLE_API_KEY'.
       b. Now install all the dependencies and libraries that we have imported in our python script.
       c. Create a Reddit App on its official website which help us to use Reddit's API to fetch the comments and posts of a user legally.
       d. Now enter all your Reddit app credentials in the code.
       e. Now choose the target_username that you want to build the persona of.
       f. Once all these steps are done you can run the code and it will create a text file with the persona of the target_username.
