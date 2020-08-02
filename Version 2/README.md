# Python-Automation-Pvt

My personal Assistant written using python

Requirement : Python 3

For doing specific tasks to help reduce work

<i>some new libraries are needed for this script to work<br>
use following instruction to install those libraries.They will be installed automatically</i>


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
    >> show sitelist                List all sites saved for faster access
    >> show processlist             List all process/apps saved for faster access
    >> show folderlist              List all folder saved for faster access
> kill                   
    >> kill                         Exit the current section
    >> kill all                     Kill all running applications in the list
    >> kill all [process]           Kill all running applications in the list except the given one
    // kill command uses force stop to terminate a process
    // any unsaved data will be lost when an app is terminated 
    // through this   

> quit / exit                       Exit the application/script
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


    ### Sending new mail and related things ###
> mail                              
    // if the mail is tried to send when internet connection is not
    // available, it will automatically try send the mail when internet 
    // connection is available
    // Only text based e-mail can be send now
    >> mail                         Access mail section
    >> help                         Get list commands in the mail section
    >> send                         Send mail from presaved mail address
    >> send new                     Send mail from preferred mail address
    >> show/show pending/show pend  Show pending mails from list
    >> show comp/show completed     Show completed mails from list
    >> show error                   Show failed mails from list
    >> show all                     Show all mails from list
    >> pending                      Return the pending mail count
    >> del / delete                   
        >>> del / delete            To delete a mail from list
        >>> del [ID]                to delete mail of given ID
    >> kill / break / stop          Exit the reminder section
    >> quit                         Exit the application
        // use keyword 'kill' to exit from sending new mail


    ### Save websites with codes for faster access of these websites  ###
> sitelist/site_list                
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
> processlist/process_list
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

> hidefile / hide_file / file_hide / filehide
    >> hidefile / filehide          Access file hiding section
    >> help                         Get list of commands in this section
    >> hide all                     Hide all files in the list
    >> unhide all                   Unhide all files in the list
    >> show                         Show files in the list
    >> show path                    Show files in the list with full location


    // use keyword 'kill' to exit from adding new process/app
    ### for internet based commads ###
> ! [command]                       
    // all commands show here all entered after the letter '!'
    // Eg: ![space][keyword]
    // site will be opened in the default web browser

    >> ! [site_code]                open website related to the code in browser
    >> ! [search_keyword]           search_keyword will be searched in google and that page will be opened in web browser

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
