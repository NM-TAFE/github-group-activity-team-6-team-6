#### 1. **Enable Debug Mode**

**How to Enable Debug Mode:**

There are several ways to enable debug mode in Flask:

- **Option A: Set Debug Mode in Code**

  Modify your `app.py` file to enable debug mode:

  ```python
  if __name__ == '__main__':
      app.run(debug=True)
  ```

  Setting `debug=True` enables the Flask debugger and the reloader.

- **Option B: Set the Environment Variable**

  You can set the `FLASK_ENV` environment variable to `development` to enable debug mode:

  For macOS/Linux:

  ```bash
  export FLASK_ENV=development
  flask run
  ```

  For Windows (Command Prompt):

  ```bash
  set FLASK_ENV=development
  flask run
  ```

  For Windows (PowerShell):

  ```bash
  $env:FLASK_ENV = "development"
  flask run
  ```

- **Option C: Use Flask CLI**

  Run the Flask application using the Flask command-line interface with the `--debug` flag:

  ```bash
  flask run --debug
  ```

#### 2. **Start the Flask Application in Debug Mode**

Once you have enabled debug mode, start your Flask application. You will see output indicating that debug mode is active and that the debugger is enabled.

Example output:

```
 * Serving Flask app 'app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

#### 3. **Trigger an Error and Use the Debugger**

When an error occurs in your Flask application while in debug mode, Flask will display an error page with a stack trace and an interactive Python shell.

- **Stack Trace**: The error page will display a stack trace showing where the error occurred in your code. This information helps you pinpoint the source of the issue.

- **Interactive Debugger**: You can use the interactive debugger to inspect variables, run expressions, and step through your code to diagnose the problem. The debugger is accessible by clicking on the console icon at the bottom right of the error page.

#### 4. **Using the Interactive Debugger**

When an exception occurs, and the interactive debugger is enabled, follow these steps to use it effectively:

- **Navigate to the Error Page**: The error page displays the stack trace and highlights the line where the error occurred.

- **Access the Interactive Shell**: Click on the console icon or the highlighted code block to open the interactive Python shell.

- **Run Commands in the Debugger**: You can now execute Python commands within the context of the current request. This feature allows you to inspect variables, run functions, and modify code on the fly.

  Example commands you might run in the debugger:

  ```python
  print(board)  # Print the current game board
  print(current_player)  # Check the current player's symbol
  ```

#### 5. **Using Breakpoints**

Breakpoints allow you to pause the execution of your Flask application at a specific point, letting you inspect the state of your application.

- **Set Breakpoints in Your Code**: Insert `breakpoint()` or `import pdb; pdb.set_trace()` into your code where you want to pause execution.

  Example:

  ```python
  def play(cell):
      breakpoint()  # This will pause execution here
      if game.board[cell] == ' ':
          game.board[cell] = game.current_player
  ```

- **Run Your Application**: When the application hits the breakpoint, it will pause, allowing you to interact with the debugger.

#### 6. **Restarting the Server Automatically**

When Flask is in debug mode, it will automatically restart the server whenever you make changes to your code. This feature allows you to see the effects of your changes without manually restarting the server.

#### 7. **Safety Note: Disable Debug Mode in Production**

Debug mode should **never** be enabled in a production environment because it can expose sensitive information and provide potential attackers with a way to run arbitrary code on your server.

**How to Disable Debug Mode:**

- Remove the `debug=True` setting in your `app.run()` call.
- Set the `FLASK_ENV` environment variable to `production`:
  ```bash
  export FLASK_ENV=production  # On macOS/Linux
  set FLASK_ENV=production     # On Windows Command Prompt
  $env:FLASK_ENV = "production" # On Windows PowerShell
  ```
