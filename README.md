## User-Persona-Builder
Hello Everyone,

I have built this project which will scrape the posts and comments from the user's Reddit profile page and create a Persona for him/her. The two files present in the repository are the results of my two different approaches to solve this problem:

* kojied.txt is the file created by running scraper.py, which runs on offline LLM.
* Hungry-Move-6603.txt is the file created by running scraper\_api.py, which uses Gemini's API.

I have used two methods for this:

1. Using Ollama's Phi model
   scraper.py is the Python script which runs on an offline LLM. In order to run that file, follow these steps:

* Install Ollama from its official website and launch it.
* Now on your terminal, run this command:
  ollama pull phi
* I am using the Phi model because my PC does not have sufficient RAM to run bigger models like Llama2 or Mistral; therefore, the result may also be compromised a bit.
* Install all the dependencies and libraries that we have imported in our Python script.
* Create a Reddit App on its official website, which will help us use Reddit's API to fetch the comments and posts of a user legally.
* Enter all your Reddit app credentials in the code.
* Choose the target\_username that you want to build the persona of.
* Once all these steps are done, you can run the code, and it will create a text file with the persona of the target\_username.

2. Using Gemini API
   scraper\_api.py is the Python script which runs on Gemini's API. In order to run that file, follow these steps:

* Create an API key for Gemini and store it in the .env file by the name:
  GOOGLE\_API\_KEY="your\_key\_here"
* Install all the dependencies and libraries that we have imported in our Python script.
* Create a Reddit App on its official website, which will help us use Reddit's API to fetch the comments and posts of a user legally.
* Enter all your Reddit app credentials in the code.
* Choose the target\_username that you want to build the persona of.
* Once all these steps are done, you can run the code, and it will create a text file with the persona of the target\_username.
