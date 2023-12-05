# Django API For C++ Inheritance Assignment

This API is built in django and is currently hosted on AWS provides basic endpoints that perform the following:

### See base url for endpoints and more info below:

- base url: 
    ```
    http://34.235.143.237:8000/
    ```

### Authentication


1. Signup endpoint:
    - url: 
        ```
        http://34.235.143.237:8000/signup/
        ```
    - response:
        Returns a token for authentication of future requests
        ```
        895bc4829a720ee314d966397a8d8edc6777e7ef
        ```

2. Login Endpoint:
    - url: 
        ```
        http://34.235.143.237:8000/login/
        ```
     - response:
        Returns a token for authentication of future requests
        ```
        895bc4829a720ee314d966397a8d8edc6777e7ef
        ```

3. Logout Endpoint:
    - url: 
        ```
        http://34.235.143.237:8000/logout/
        ```
     - response:
        Generated token for user gets destroyed
        ```
        {"message": "logout was successful"}
        ```

### Course CRUD Operation Endpoints 

1. Create course endpoint:
    - url:
        ```
        http://34.235.143.237:8000/course/create-course/
        ```
    - response:
        ```
        {"Success": f"The course {name} was successfully deleted"}
        ```

2. Delete course endpoint:
    - url:
        ```
        http://34.235.143.237:8000/course/delete-course/<int:course_id>/
        ```
    - response:
        - success:
            ```
            {"Success": f"The course {name} was successfully deleted"}
            ```
        - error:
            ```
            "Error": f"course with id '{course_id}' not found"
            ```

3. Get all courses endpoint:
    - url:
        ```
         http://34.235.143.237:8000/course/get-all-courses/
        ```
    - response:
        ```
        [{"id":1,"title":"django","course_code":"dj101"},{"id":3,"title":"jsmastery","course_code":"js201"}]
        ```

4. Update course endpoint:
    - url: 
        ```
         http://34.235.143.237:8000/course/delete-course/
        ```
    - response:
        - success:
            ```
            {"Success": f"The course was successfully updated"}
            ```
        - error:
            ```
            {"Error": f"course with id '{request.data.get('course_id')}' not found"}
            ```