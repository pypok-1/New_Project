### <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDR4eGFnb2dlMjd0bjE5MnZnNWg5NnFmYXFsbjA0bzd4ZmYwNzJ4bSZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/YnkMcHgNIMW4Yfmjxr/giphy.gif" width="50"> Django Comments System 💬>

---

## 🚀 Основні функції:
- **CRUD операції** для коментарів: Створення, Читання, Оновлення, Видалення
- **Class-Based Views**: ListView, DetailView, CreateView, UpdateView, DeleteView
- **Authentication**: Логін-обов'язкові дії через `LoginRequiredMixin`
- **Permissions**: Користувач може редагувати/видаляти тільки свої коментарі
- **URL Routing**: Динамічні URL з параметрами (`post_id`, `id`)
- **Шаблони**: Власні HTML-шаблони для кожної сторінки

---

## 📁 Структура проекту:

comments/
├── models.py 
├── views.py 
├── urls.py 
├── templates/ 
│ └── comments/
│ ├── comment_list.html 
│ ├── comment_detail.html 
│ ├── comment_form.html 
│ └── comment_delete.html 
