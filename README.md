<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro&family=Literata" rel="stylesheet">

<div align=center>
<img src="images/icon.png" alt="icon.png" width="200" height="200">
<h1>Reminder-Bot</h1>
  
## Description
Reminder-Bot is a Discord bot that allows users to keep track of what tasks they have throughout the week or even today. In addition, if the user is in the database, it tells you what tasks you planned on that given day by sending you a direct message. This bot uses a database coded in SQL and keeps track of the user and their preference when they want to be messaged in the morning. In addition, it keeps track of the user's task and if they are completed or not.
</div>


<div align=center>
  
## How to install

</div>

Not interested in downloading bot to your computer, you can add bot to your server [here](https://discord.com/oauth2/authorize?client_id=1214322771765497916&permissions=21983791152192&scope=bot)

Follow these steps to run the Discord application and add it to your server.
1. If you are *not* an author, fork the repository [here](https://github.com/pedropa140/Reminder-Bot/fork).
2. Clone the repository.
    ```bash
    git clone https://github.com/pedropa140/Reminder-Bot.git
    ```

3. Install Dependencies
   - Make sure your pip version is up-to-date:
      ```bash
      pip install --upgrade pip
      ```
      ```bash
      pip install -r requirements.txt
      ```
3. Create Discord Application <br>
    - Go to [https://discord.com/developers/applications](https://discord.com/developers/applications)
    - Click on **New Application**
    - Give it a name
    - Agree to [Developer Terms and Services](https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service) and [Developer Policy](https://discord.com/developers/docs/policies-and-agreements/developer-policy)
    - Go to the **Bot** tab
      - Click on **Reset Token** to receive Discord Application Token
      - Go back to the Github clone and create a **.env** file
      - Type
        
        ```bash
        DISCORD_TOKEN = '**REPLACE WITH DISCORD TOKEN THAT YOU JUST COPIED**'
        ```
    - Go to the **OAuth2** tab
      - For **OAuth2 URL Generator**, click on **bot** on the second column
        - For **General Permissions**, click on
          - **Read Messages/View Channels**
          - **Manage Events**
          - **Create Events**
          - **Moderate Members**
          - **View Server Insights**
          - **View Creator Monetization Insights**
  
      
        - For **Text Permissions**, click on
          - **Send Messages**
          - **Create Public Threads**
          - **Create Private Threads**
          - **Send Messages in Threads**
          - **Send TTS Messages**
          - **Manage Messages**
          - **Manage Threads**
          - **Embed Links**
          - **Attach Files**
          - **Read Message History**
          - **Read Message History**
          - **Mention Everyone**
          - **Use External Emojis**
          - **Use External Stickers**
          - **Add Reactions**
          - **Use Stash Commands**
          - **Use Embedded Activities**
  
      
        - For **Voice Permissions**, click on
          - **Use Embedded Activites**
  
            
      - Copy the **Generated URL** and paste it in your web browser.
      - Click on the Discord server you would like to add the bot into.
        
<div align=center>   
  
## How to run the Reminder-Bot

In a terminal, find the directory where main.py is located and run this command:
</div>

  ```bash
  python main.py
  ```

### Options:
  - **@Reminder-Bot !hello**
    - returns a friendly greeting! 
  - **@Reminder-Bot !time**
    - tells the current time.
  - **@Reminder-Bot !adduser**
    - adds user to the database.
  - **@Reminder-Bot !userinfo**
    - returns user information from the database.
  - **@Reminder-Bot !changereminder**
    - changes the time that the user wants to be notified of the tasks.
  - **@Reminder-Bot !deleteuser**
    - deletes user from the database.
  - **@Reminder-Bot !addtask**
    - adds a task to the task list.
  - **@Reminder-Bot !todaytask**
    - displays the tasks that end on the current date.
  - **@Reminder-Bot !alltasks**
    - shows all uncompleted tasks.
  - **@Reminder-Bot !removetask**
    - removes tasks from tasks list.
  - **@Reminder-Bot !completetask**
    - updates an uncompleted task into completed.
  - **@Reminder-Bot !pomodoro**
    - initializes the pomodoro method.
  - **@Reminder-Bot !help**
    - shows the help menu.