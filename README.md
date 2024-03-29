# Python-Automation-Pvt

My personal Assistant written using python

> <li>Required : Python 3.7 <br>

> You must have internet connection when starting this script for the first time<br>
> It will automatically install some missing modules<br>

> Read '<I>README.md</i>' inside each version for detailed command list


## <u>Version 3</u>

Features :-
    <li>Folder Fast Access</li>
    <li>App Fast Access</li>
    <li>Website Fast Access</li>
    <li>Adding Reminders</li>
    <li>Keeping record of movies and series</li>

<u><b>Command List</b></u>

PS : commands are not case sensitive/ typing in upper and lower case have the same effect<br>
PS : In sections like processlist,sitelist , it will need to restart the app for the effect to take change after adding a new item

```
> help                              Show the list of commands in each section
> [process_keyword]                 Will start the app related to the kwyword/processcode
> show
    >> show                         Show the list of files in the current directory
    >> show [keyword]               Show the list of files in the location given for the keyword
        >>> Eg :- show english      List all items in the folder saved for faster access with keyword 'english'
    >> show reminder                List all pending reminders
    >> show mail                    List all pending e-mails
    >> show site                    List all sites saved for faster access
    >> show app                     List all process/apps saved for faster access
    >> show folder                  List all folder saved for faster access
	>> show media					List all media
    >> show media gui               Open GUI
	>> show media status			Shows statitics of all media you watched
> kill                   
    >> kill                         Exit the current section
    >> kill all                     Kill all running applications in the list
    >> kill all [process]           Kill all running applications in the list except the given one
    // kill command uses force stop to terminate a process
    // any unsaved data will be lost when an app is terminated 
    // through this   
> add
	>>	add app						Add an app to app fast access
	>>	add app	gui					Add an app to app fast access but GUI mode
	>>	add site					Add an site to website fast access
	>>	add site gui				Add an site to website fast access but GUI mode
	>>	add folder					Add an folder to app fast access
	>>	add folder gui				Add an folder to app fast access but GUI mode
	>> 	add med						Add an media to your watched list

> configure / configure				open configuration panel
> config gui						open configuration panel GUI mode

> con?                              Check if interconnection is available
> quit / exit                       Exit the application/script
> play [type] [filename]            play the media file  ### DISABLED
> path                              Show current path
> set path [path]                   Set new path
> sd [foldername]                   Enter that folder if it exists in the current directory
> open
    >> open                         open current directory/location/path
    >> open [foldername/filename]   open specified folder/file it is exits
    >> open [keyword]               open the location saved in that keyword for faster access
> cmd                               
    >> cmd                          open CMD
    >> cmd [command]                Run CMD commands
> con?                              Check id internet connection is available
> clear                             
    >> clear                        Clear terminal
    >> clear temp                   Clear temporary system files
> change enc                        To change encryption
> change pass                       To change password
> login                             To login using the password
    // if the given password is correct, you logged in to the master account
    // all the hidden files will be shown and accessible now
    // if the password is incorrect, it wont show incorrect. instead it will log in to user
    // account . The effect will be files in the hidden section will be stay hidden 
    // and cannot be accessed directly


    ### Adding reminder/task and related things ###
> reminder                          
    >> reminder                     Access reminder section
    >> help                         Get list commands in the reminder section
    >> add/new                      Add new reminder
    >> show/show pending/show pend  Show pending task/reminder from list
    >> show [type]                  show all pending reminder/task of the given type
    >> show comp / show completed   Show completed task/reminder from list
    >> show all                     Show all task/reminder from list
    >> show all [type]              show all reminder/task of the given type
    >> pending                      Return the pending task/reminder count
    >> del / delete                   
        >>> del / delete            To delete a reminder/task from list
        >>> del [ID]                to delete task of given ID
    >> kill / break / stop          Exit the reminder section
    >> quit                         Exit the application
    >>> adding new reminder example
        reminer/task :      // enter the reminer
        type :              // type of the reminder
        // suppose i have Visual Studio installed in the keyword 'code'
        // if i add reminder of type 'code', when i launch Visual studio through this CLI 
        // all the reminders with type 'code' will be shown

        // use keyword 'kill' to exit from adding new reminder




    ### Save websites with codes for faster access of these websites  ###
> sitelist/site_list/site                
    >> sitelist / site_list         Access sitelist section
    >> help                         Get the list of commands in this section
    >> show                         Show all sites saved for for faster access
    >> del / delete
        >>> del/delete              To delete a site from list
        >>> del [site_code]         to delete site of given site code
    >> add/new                      Add new website for faster access
    >>> adding new website example
        Website Title : GitHub
        Website : https://github.com/Shishere007
        Enter website codes seperated by coma
        Website code : git,github
        // here you will be able to access the above site by both keywords git & github
        // use keyword 'kill' to exit from adding new website


    ### Save process/apps with code for faster access ###  
> processlist/process_list/app
    >> processlist/process_list     Access processlist section
    >> help                         Get list commands in this section
    >> add / new                    Add new app/process for faster access
    >> del / delete                 Delete an app/process faster access list
    >> show                         List all the process/apps saved for faster access
    >>> adding new process
        Process Title : Visual Studio Code
        Process location(full) :  \..\Programs\Microsoft VS Code\Code.exe
        Process Codes : code,vscode

        // Now will be able to access visual studio code through this app with keywords
        // code & vscode

        // use keyword 'kill' to exit from adding new process/app


    ### Add folders for faster access ###
> filelist/file_list/folderlist/folder_list
    >> filelist/folderlist          Access folder fast access section
    >> help                         Get list commands in this section
    >> add / new                    Add new folder for faster access
    >> del / delete                 Delete an folder faster access list
    >> show                         List all the folder saved for faster access
    >>> adding new folder for faster access
        Folder Title : Python Codes
        Folder location(full) :  D:\Code\Python
        Folder Codes : python,pcode

        // Now will be able to access 'Python Codes' folder through  this app with keywords
        // python/pcode

        // use keyword 'kill' to exit from adding new process/app



    // use keyword 'kill' to exit from adding new process/app
    ### for internet based commads ###
> ! [command]                       
    // all commands show here all entered after the letter '!'
    // Eg: ![space][keyword]
    // site will be opened in the default web browser

    >> ! [site_code]                open website related to the code in browser
    >> ! [search_keyword]           search_keyword will be searched in google and that page will be opened in web browser
> media
	>>	add							add new media to watched list
	>>	show [categoey]				show media saved under the category
	>> 	show cat/category			show list of categories
	>> 	add cat/category			add new categoey
	>> 	status						media statitics
	>>	help						command help
> Other Buit-in Commands
    >> tasklist                     List all running tasks
    >> tasklist det                 List all running tasks with full detail
    >> shut / shutdown              Shutdown PC
    >> hiber / hibernate            Hibernate PC
    >> logoff                       Log off current user
    >> restart                      Restart PC
    >> groov / groove / gr          Start Groove Music if exists
    >> cam / camera                 Start Camera if available
```