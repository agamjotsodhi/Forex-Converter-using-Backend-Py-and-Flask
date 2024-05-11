# **Conceptual Exercise**


## 1. What are important differences between Python and JavaScript?**

**Sytanx**
  one major difference between the two is that altough they both excute the same concepts, the way they are written differ. Python is more simplified and shorter in nature compared to javascript. The way you write certin concepts between the two differ. For example in javascript when we define variabe we say let x = 0, and in python we simply do x = 0. There are many small syntax differences like creating functions, in JS we say function test (){} and in Python we say def test (): .
  
 **Use Cases**
  Another key difference is that javascript is typically used for web development and adding functionality to html/css, thus being catered to front end usecases. Where python is typically more flexiblle in nature and can be applied in diverse use cases, typically backend development. 

  ## 2. Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  ##    can try to get a missing key (like "c") *without* your programming crashing
  
  1. to return a default value when a key is not found, in this case we can pass a value that says:
    value = dict_name.get("c", "Key not found")
    print(value)

  2. another option we have is that we can setdefault(key[, default]). When a key cannot be found in a dict, setdefault will return a value of default/none
   
 ## 3. What is a unit test?
  Unit testing is when we test individual pieces of code to see if they work on there own. Similar to testing each part of a car on it's own.

 ## 4. What is an integration test?
 Intergration testing is when we test different pieces of code joined together to see if they work well with each other. An example of this would testing a car engine that has many different parts working together, to see if they ultimately start the engine. 

 ## 5. What is the role of web application framework, like Flask?
 Web application frameworks like Flask and Django act like toolboxes for websites and provide an existing structures. Thesse structures take care of tasks that otherwise would take longer for a developer to hardcode. These tasks include pre-built functions, simplyfing and handling web requests and managing data. 

 ## 6. You can pass information to Flask either as a parameter in a route URL
 ##    (like '/foods/pretzel') or using a URL query param (like
 ##   'foods?type=pretzel'). How might you choose which one is a better fit
 ##    for an application?

  The best way to choose which method is better suited for an application would be to look at the nature of information you are displaying on your app. If your app focuses more on displaying straight forward information that simply jumps from one page to another, passing it as a parameter in the url is a good idea.

  If your information requires passing in terms/search bars/optinal/filtered info, a URL parameter will be a better option to showcase data.  

 ## 7. How do you collect data from a URL placeholder parameter using Flask?
  Using flask to collect data from a URL placeholder parameter, you would define a route with a placeholder in the url. For ex. you would write: (/user/<username>) and access the parameter using request.args.get('username')

  ## 8. How do you collect data from the query string using Flask?
 To collect data, we would use: request.args.get('type') and pass in the value that type= in the url.

  ## 9. How do you collect data from the body of the request using Flask?
 To collect data from the body, we would request.json to access JSON data or request.form to access form data submitted from a POST request.

 ## 10. What is a cookie and what kinds of things are they commonly used for?
 cookies are small pieces of data that are stored in the user's browser by a website. They are useful for storing user preferences, session identifiers, or tracking information. A common example would be remebering a user's login cred so they would'nt have login more than once. 

 ## What is the session object in Flask?
 A session object in Flask is like a personal notebook that the website keeps for each visitor. It's used to remember things about you, like your username or preferences, while you're on the site. This way flask remebers information about the user when the comeback to a certin page after jumping to multiple pages.

 ## What does Flask's `jsonify()` do?
 Flask's jsonify() function converts Python dictionaries into JSON-formatted responses, making it easy to return JSON data from Flask routes.
 
