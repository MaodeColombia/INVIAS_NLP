Evitar que se corra `!pip install openai` cada vez que se corre el código; código generado por ChatGPT. 

---

**How to Use It**
- Run the script in your Jupyter Notebook or Python environment.
- It will:
  1. Check if the package is installed.
  2. Compare the installed version with the latest version available.
  3. Print appropriate messages or take action.

---

**Example Output**
1. **Package is Installed and Up-to-Date:**
   ```
   ✅ openai is already installed (version: 0.27.8).
   ✅ openai is up-to-date.
   ```

2. **Package is Installed but Outdated:**
   ```
   ✅ openai is already installed (version: 0.27.8).
   ⚠️ A new version of openai is available: 0.28.0.
   ```

3. **Package is Not Installed:**
   ```
   🔄 Installing openai...
   ✅ openai has been installed.
   ```

4. **Network Issues:**
   ```
   ⚠️ Unable to fetch the latest version. Please check your network.
   ```

---