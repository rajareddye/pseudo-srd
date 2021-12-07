# pseudo README

SRD Pseudocode syntax highlighter and pseudo language custom formatter .

## Features

Prerequisites.
 
  Install 'Visual Studio Code’ from Appstore
 
  Install vscode extensions ‘pseudo-pspec’, ‘vscode-icons’ and 'Custom Local Formatters'.
  
  Convert SRD docx to *.pseudo files using ‘extract_all_pspecs.py’  (SRD.docx markups should be in accepted state).
  
  For .pseudo files formatting, place 'format_pseudo_files.py' in root of your workspace folder and register this by updating vscode settings as mentioned below
  ''' vscode settings.json 
  {
    "customLocalFormatters.formatters": 
	 [        
		{
      "command": "python format_pseudo_files.py",
      "languages": ["pseudo"]
		}
	 ]
  }  
  
    "customLocalFormatters.formatters": [
    {
      "command": "python %USERPROFILE%\\.vscode\\extensions\\pseudo-srd.pseudo-0.1.3\\format_pseudo_files.py",
      "languages": ["pseudo"]
    }
  ],
  
  '''
  this will enable vscode formatting for pseudo language (alf+shift+f). 
 


## known issues:

