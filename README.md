# User Input
## API
```
class UI {
    /**
    * Register a function code
    *
    * @param _fc        a unique string (regex: r"\w+") which represents the callback
    *                   _fc will be extracted from the 1st token in user command line input
    *
    * @param _handler   a callable object which accept a list-like object as its only parameter
    *                   _handler(args) will be called when _fc is detected from user input
    *
    * @param _desc      Description of the function code
    *
    * @return None
    */
    void register(const char * _fc, const void * _handler, const char * _desc) {}

    /**
    * Process user command line input
    * 1. Get user command line input
    * 2. Split the input into an array of strings (sep="\s")
    * 3. Detect function code (the 1st element of the array)
    * 4. Call corresponding handler of the function code
    *
    * @return None
    */
    void def process() {}

    /**
    * Print to console the list of function codes, and their descriptions
    *
    * @return None
    */
    void print_help() {}
}

```
## How to use
* Step 1: To import UI class from ui
    ```from ui import UI```

* Step 2: To create an instance of UI class
    ```m_ui = UI()```

* Step 3: to register function code, handler function, and a description
    ```
    ## \brief Function f0
    # f0 will be used as callback handler for function code "f0"
    # \param args a list-like object (None is accepted)
    def f0(args):
        # Do something
        pass

    m_ui.register('f0', f0, 'This is function f0')
    ```
* Step 4: call process() method to read user input, and call the corresponding handler
