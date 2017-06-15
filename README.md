# glowing-journey

This task was done for a technical interview

## How to

First clone the repository

`cd /tmp`  
`git clone https://github.com/Lepthy/glowing-journey.git`  
`cd glowing-journey`  

Bootstrap application

`bash bootstrap.sh`  

Then point a browser to
> http://localhost:8000/static/index.html

You will find a selector and a input field.
The selector allows attribute filtering in the search (ANY for any attributes).
The input field is a substring to match in the attribute.

The output tag will update with every keystroke, reducing the response payload with every additional letter.

## TODO
1. Reduce size of response with size parameter and last_key
2. Expose in front-end app multi attribute search (supported by the server)
3. Get list of attributes from the server (for the selector)
4. Async the tornado server
5. Add Dockerfile
6. COMMIT EVERY STEP Q_Q
