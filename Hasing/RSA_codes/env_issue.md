He can run it with just:

```
python3 rsa_ctf.py
```

**ONLY because his Python3 already had `Crypto` installed.**
Your system Python **does NOT**, because Kali uses Python 3.13 and the package is not available for it.

But once you activate the virtual environment, **your `python` and `python3` commands will point to the venv**, exactly like in the video.

So after activating the venv, **you CAN run it the same way**.

---

# ✅ Do This (exact commands to copy‑paste)

### 1️⃣ **Create the virtual environment (only once)**

```bash
python3.13 -m venv ~/pyenv
```

### 2️⃣ **Activate it (do this every time you want to run the script)**

```bash
source ~/pyenv/bin/activate
```

Your terminal prompt should now look like:

```
(pyenv) ┌──(samin㉿kali)-[~]
```

### 3️⃣ **Install Crypto inside the venv**

```bash
pip install pycryptodome
```

### 4️⃣ **Now run your script EXACTLY like the video:**

Go to the directory:

```bash
cd /home/samin/Documents/Codes
```

Run:

```bash
python3 rsa_ctf.py
```

or even:

```bash
python rsa_ctf.py
```

---

# 🎉 Now it will work exactly like the video

Because inside the venv, `python3` == Python 3.13 **with Crypto installed**.

---

If you want, I can also help you make the venv **activate automatically** when you enter the folder.
