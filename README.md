## Flask Application Design

### HTML Files

**index.html**
- Responsible for displaying the main user interface.
- Includes Bootstrap for styling and layout.
- Contains a form for adding tasks and a list to display existing tasks.

**Content:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>To-Do App</title>
</head>
<body>
  <div class="container">
    <h1>To-Do List</h1>
    <form id="task-form">
      <div class="form-group">
        <label for="task">Task:</label>
        <input type="text" class="form-control" id="task" name="task">
      </div>
      <button type="submit" class="btn btn-primary">Add Task</button>
    </form>
    <ul id="task-list" class="list-group">
    </ul>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  <script src="app.js"></script>
</body>
</html>
```

### Routes

**app.py**
- Defines the routes and logic for the application.

**Routes:**

- `/`: Root route that displays the main `index.html` page.
- `/add-task`: Route for handling the submission of new tasks.
- `/remove-task`: Route for handling the removal of existing tasks.