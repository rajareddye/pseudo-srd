# pseudo README

> Pseudocode syntax highlighter (SRD in pspec files)

## Features

> > Here are the steps to view SRD pseudo code in microsoft ‘visual studio code‘
> >
> > > Step*1 : Install latest 'Visual Studio Code’ from Appstore
> > > Step_2 : After installation launch the ‘Visual Studio Code ‘ . Goto extensions and then search for ‘pseudo-pspec’ and install .
> > > Step*3 : Using ‘extract_all_pspecs.py’ convert SRD docx to \*.pseudo files and folders. Before use this script save the word by accepting all markups.
> > > Goto converted pseudo file folder and select open with ‘visual studio code’ . you get the SRD in VSCode

> > Note : files with long path is very well handled by ‘visual studio code’.
> > Screen shot of SRD \*.pseudo

## known issues:

> > you need to enable windows long path .
> > windows version of VSCode does not search in long path files. due to regex constraint.
> > Linux version of VSCode does not have long file path issues, It works well.
>
> > To Enable long path run the below command in power-shell in administrator mode

> > > New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
