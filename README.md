# My First .NET Project 🚀

This is my very first .NET project! 🎉  
I’m using **.NET SDK** and **SQLite** as my database while learning the basics of C# development.

---

## 📦 Prerequisites (on Arch Linux)

Make sure your system is updated:

```bash
sudo pacman -Syu
```

### 1. Install .NET SDK
Arch Linux has official packages for .NET:

```bash
sudo pacman -S dotnet-sdk
```

Verify installation:

```bash
dotnet --version
dotnet --info
```

### 2. Install .NET Runtime (optional, if only running apps)
```bash
sudo pacman -S dotnet-runtime
```

### 3. Install SQLite
SQLite will be used as the database engine:

```bash
sudo pacman -S sqlite
```

Check version:

```bash
sqlite3 --version
```

---

## 🛠️ Setup Project

Create a new console app:

```bash
dotnet new console -o MyFirstApp
cd MyFirstApp
```

Add SQLite support with **Entity Framework Core**:

```bash
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Tools
```

---

## ▶️ Run the App

To build and run:

```bash
dotnet run
```

---

## 📝 Notes

- I’m using **SQLite** because it’s lightweight and perfect for learning.
- I’ll be experimenting with **C# basics, database connections, and EF Core**.
- This repo is for learning purposes — expect mistakes and growth! 🚀

---

## 📚 Resources

- [.NET Documentation](https://learn.microsoft.com/dotnet/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [EF Core with SQLite](https://learn.microsoft.com/ef/core/providers/sqlite/)
