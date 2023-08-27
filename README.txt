install miniconda3
https://docs.conda.io/en/latest/miniconda.html

install packages youll need
pip install dash discord.py

install vs code
https://code.visualstudio.com/docs?dv=win

============================================
Add Conda to PATH Manually:

a. Open the Start menu, search for "Environment Variables," then choose "Edit the system environment variables."

b. In the System Properties window, click on the "Environment Variables" button.

c. In the "Environment Variables" window, highlight the Path variable in the "System variables" section and click the Edit button.

d. Add these two paths to the end of the list (you can use the semicolon ; as a delimiter between paths):

makefile
Copy code
C:\Users\xanar\miniconda3
C:\Users\xanar\miniconda3\Scripts

=================================================
Configure VS Code to Use Conda Environment Directly:

a. In VS Code, click on the gear icon (⚙️) in the lower left corner and select "Settings."

b. Search for "Python Terminal Activate Environment" and make sure it's checked.

c. When you start a terminal within a Python project, VS Code will automatically activate the selected Python environment.

=================================================
Use Command Prompt or another Terminal:

If you don't necessarily want to use PowerShell, you can configure VS Code to use Command Prompt or another terminal of your choice:

a. Open the Command Palette in VS Code with Ctrl+Shift+P.

b. Type "Select Default Shell" and select it from the dropdown list.

c. Choose the desired shell (e.g., Command Prompt).


==========================================
New keybindings
Ctrl+K Ctrl+s
{
        "key": "ctrl+j",
       "command": "workbench.action.focusActiveEditorGroup"
    },
    {
        "key": "ctrl+k",
        "command": "workbench.action.terminal.focus"
    }
