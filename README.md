# pseudo README

SRD Pseudo code syntax highlighter for ‘Visual Studio Code’

## Features

These are the steps to view SRD pseudo code in microsoft ‘visual studio code‘ , which is free and rich code editor with more options.
Step_1 : Install latest 'Visual Studio Code’  by downloading from website Download Visual Studio Code - Mac, Linux, Windows you can use System Installer.
               Offline installer is included for convience ‘VSCodeSetup-x64-1.60.0.exe.zip’ .you can aslo install this.
Step_2 : After installation launch the ‘Visual Studio Code ‘ . Goto settings and select extensions  and then search for ‘pseudo-pspec’ and ‘vscode-icons’ extensions and install them.
	You can also install these plugins manually with attached pseudo-0.1.2.vsix.zip, using command ,
	Goto view open Command Palette  run the command ‘Extensions: Install from VSIX ‘ and Select the file : *.vsix from the attached file
Step_3 : Using ‘extract_all_pspecs.py’ convert SRD docx to *.pseudo files and folders.
	Now right_click on the folder and select open with ‘visual studio code’ . you search all the *.pseudo  pspec files in the same as word document.

Note : files with long path is very well handled by ‘visual studio code’.
	Screen shot of SRD *.pseudo 

# known issues:
you need to enable windows long path .
If you have any « file not found error« , Then run the below command in power-sheel in administrator mode
run the below command .
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
