# 🧹 Setup File Cleaner

**Setup File Cleaner** is a lightweight Python utility that recursively scans a given directory for `.exe` and `.msi` files typically related to installations (e.g., `setup`, `installer`, etc.), displays their sizes, and offers the user an option to safely delete them.

This tool is ideal for cleaning up download folders or disk clutter caused by leftover installation files.

⚠️ Note: This tool is intended for use on Windows systems, as it targets .exe and .msi files.
---

## 📂 Features

- ✅ Recursively scans directories  
- ✅ Detects `.exe` and `.msi` files with installation-related names  
- ✅ Displays file paths and sizes in MB  
- ✅ Asks for confirmation before deletion  
- ✅ Logs deletion success and errors  

---

## 🚀 Usage

### Prerequisites

- Python 3.x installed

### Running the script

From your terminal or command prompt:

```bash
python clean.py /path/to/your/target/directory
```

#### Example on Windows:

```bash
python clean.py "C:\Users\YourName\Downloads"
```

---

## 🧠 How It Works

1. **Scans** the provided directory recursively for `.exe` and `.msi` files.
2. **Filters** files that contain any of the following keywords in their filename (case-insensitive):
   - `setup`, `stp`, `install`, `installer`, `installation`
3. **Displays** a list of found files with their sizes.
4. **Prompts** the user for confirmation before deletion.
5. **Deletes** the selected files and logs each result.

---

## 🔐 Safety Notes

- No files are deleted without **explicit confirmation**.
- If the script fails to delete a file (due to permissions or locks), it will log the error and continue.

---

## ⚖️ License

This project is released under the [MIT License](LICENSE). Feel free to use, modify, or share it.

---

## 👤 Author

Developed by Danilo Radosavljević — a minimal CLI tool made with love for system hygiene and scripting practice.

---

## 💡 Tip

Want to test it first without deleting anything? Comment out the `os.remove(path)` line in the `clean()` function to do a **dry run**.
