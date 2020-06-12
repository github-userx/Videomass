; Script generated by the Inno Setup Script Wizard.
; Edited by Gianluca Pernigotto
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Videomass"
#define MyAppVersion "2.1.0 (64-bit)"
#define MyAppPublisher "Gianluca Pernigotto"
#define MyAppURL "http://jeanslack.github.io/Videomass/"
#define MyAppExeName "Videomass.exe"
#define MyAppIcoName "videomass.ico"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1608E2C6-6B13-4793-A9A6-6283E3BF1305}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\gianluca\Documents\Videomass\DOC\COPYING
InfoBeforeFile=C:\Users\gianluca\Documents\Videomass\DOC\NOTICE.rtf
InfoAfterFile=C:\Users\gianluca\Documents\Videomass\DOC\AUTHORS
OutputDir=C:\Users\gianluca\Documents
OutputBaseFilename=Videomass-v2.1.0-py3-x64-Setup
SetupIconFile=C:\Users\gianluca\Documents\Videomass\art\videomass.ico
Password=
Compression=lzma
SolidCompression=yes
CreateAppDir=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags:

[Files]
Source: "C:\Users\gianluca\Documents\Videomass\Videomass.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\gianluca\Documents\Videomass\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppIcoName}"; WorkingDir: "{app}"
Name: "{group}\Uninstall Videomass"; Filename: "{uninstallexe}"
Name: "{group}\Website"; Filename: "https://jeanslack.github.io/Videomass/"

Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}";IconFilename: "{app}\{#MyAppIcoName}"; Tasks: desktopicon
; Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}";IconFilename: "{app}\{#MyAppIcoName}";
; Name: "{commonstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}";IconFilename: "{app}\{#MyAppIcoName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

