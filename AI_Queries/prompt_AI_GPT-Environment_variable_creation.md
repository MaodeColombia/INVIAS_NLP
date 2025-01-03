# Process to Create an Environment Variable in Windows

Below is the step-by-step description of how you created the environment variable, including details for each step. You can include screenshots from your setup process to make the explanation clearer.

---

### Step 1: Open the Environment Variables Window
1. Press **`Win + S`** to open the search bar.
2. Type **"variables de entorno"** and click on **"Edit the system environment variables"** in the search results.
3. In the **System Properties** window, go to the **Advanced** tab and click on **Environment Variables**.

---

### Step 2: Create or Edit a User Variable
1. In the **Environment Variables** window, look under the **User variables** section for your username.
2. Click on **New** to create a new variable or **Edit** to modify an existing one.

---

### Step 3: Define the Variable Name and Value

> see [openai api_key creation](../assets/images/20250103_115821.png), [environment varialble creation](../assets/images/20250103_134239.png)

1. In the **Edit User Variable** or **New User Variable** dialog:
   - **Variable Name**: Enter the name of the variable. In your case, it was `OPENAI_API_KEY`.
   - **Variable Value**: Paste the API key value provided by OpenAI.

   **Example**:
   - Variable Name: `OPENAI_API_KEY`
   - Variable Value: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

2. Click **OK** to save the variable.

---

### Step 4: Confirm the Variable Exists
1. After saving, look for the variable (`OPENAI_API_KEY`) in the list under **User variables**.
2. Verify that the name and value appear correctly.

---

### Step 5: Restart Your Applications
1. Close any open Command Prompt, PowerShell, or IDE (e.g., Visual Studio Code) instances.
2. Reopen them to ensure the environment variable is loaded into your session.

---

### Step 6: Test the Environment Variable
To ensure that the variable is accessible, you can test it in Python or the Command Prompt.

- Command Prompt:
  ```cmd
  echo %OPENAI_API_KEY%
  ```

- Python:
  ```python
  import os
  print(os.environ.get("OPENAI_API_KEY"))
  ```

---

### Step 7: Use the Variable in Your Python Script
Once confirmed, you can use the environment variable in your Python code like this:
```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
    print("API key loaded successfully!")
else:
    print("API key not found!")
```

---

This step-by-step guide provides a detailed overview of the process. Let me know if you need help organizing the screenshots or adding more details! 😊