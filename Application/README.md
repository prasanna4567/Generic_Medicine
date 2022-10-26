### Basic Setup Requirements
1. Set home directory as `Application` directory using `cd Application` command

2. Install Latest Python version from https://www.python.org/downloads/
    - Set system environment variables for Python.exe, pip.exe (https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables)
    - Verify python installation using command `python --version`
    - Verify pip availability using command `pip --version`

3. Setup Flask
    - Set environment for flask project using commands `set FLASK_APP=app` and `set FLASK_ENV=development`
    - Create a project folder and change directory to the project directory using command `cd`
    - Install Flask using `pip install flask`
    - Verify flask version using the command `python -c "import flask; print(flask.__version__)"`
    - Copy `app.py` file from ``

4. Run Flask Application
    - Run Flask application using `flask run`
    
    
### Project Structure

1. Application
    - `app.py` is the driver file for the application.
    - By default UI templates are kept inside `templates` folder which will be automatically picked by framework
    - Styles, Scripts are kept inside `static` folder
2. Framework
    - `static` folder will have styles including the custom styles and bootstrap
    - Using `Bootstrap`, `Jquery` frameworks for UI
    - Bootstrap downloaded and kept with the project, so local development loading will be faster.

### How to use project

1. You can use following routes `localhost:5000/`, `localhost:5000/first` and `localhost:5000/first`
2. More updates to come...



Thank you :blush:
