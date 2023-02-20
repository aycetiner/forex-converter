### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is a general-purpose, high-level programming language with a strong emphasis on readability and simplicity, while JavaScript is a scripting language that is mainly used for web development and is designed to be run on a web browser. Python is typically used for server-side scripting, machine learning, and scientific computing, whereas JavaScript is typically used for client-side scripting and creating interactive web pages.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

Two ways to avoid crashing when accessing a missing key in a Python dictionary are to use the get() method, which returns a default value if the key is missing, or to use a try-except block to catch the KeyError exception that would be raised if the key is not present.

- What is a unit test?

A unit test is a type of software testing where individual units or components of a software application are tested in isolation to ensure that they are working as expected.

- What is an integration test?

An integration test is a type of software testing where different components of a software application are tested together to ensure that they are working as expected when integrated.

- What is the role of web application framework, like Flask?

A web application framework like Flask is a collection of tools and libraries that provides developers with a standardized way to build web applications. Flask, in particular, is a lightweight framework that makes it easy to build small to medium-sized web applications in Python.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

The choice between using a route parameter or a URL query parameter in Flask depends on the type of data being passed. Route parameters are better suited for data that is required to fulfill a request, while query parameters are better suited for optional or supplementary data.

- How do you collect data from a URL placeholder parameter using Flask?

To collect data from a URL placeholder parameter using Flask, you can define a route with a parameter enclosed in angle brackets, like <parameter_name>, and then pass it to the funtion as an argument to have access to it. For example:

"""
@app.route('/users/<int:user_id>/likes')
@check_auth
def users_likes(user_id):
"""Show list of followers of this user."""

    user = User.query.get_or_404(user_id)
    likes = [like.id for like in g.user.likes]

    return render_template('users/likes.html', user=user, likes=likes)

"""

- How do you collect data from the query string using Flask?

To collect data from the query string using Flask, you can access the query parameters in the view function using request.args.get('parameter_name').

- How do you collect data from the body of the request using Flask?

To collect data from the body of the request using Flask, you can access the request body in the view function using request.data or request.get_json().

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a small text file that a website stores on a user's device to remember their preferences or login information. Cookies are commonly used for tracking user activity, storing shopping cart items, and personalizing website content.

- What is the session object in Flask?

The session object in Flask is a way to store user-specific information across multiple requests. It uses cookies to store a unique session ID on the user's device, and then stores the session data on the server.

- What does Flask's `jsonify()` do?

Flask's jsonify() function is a utility that serializes a Python object into a JSON-formatted string and returns a Flask response object with the appropriate content type header. This is useful for returning JSON data from a Flask view function.
