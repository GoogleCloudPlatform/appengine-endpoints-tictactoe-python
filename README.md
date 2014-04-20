## Added some features

appengine-endpoints-tictactoe-python
====================================

This application implements a simple backend for a Tic Tac Toe game using
Google Cloud Endpoints, App Engine, and Python.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions

1. Make sure to have the [App Engine SDK for Python][4] installed, version
   1.7.5 or higher.
2. Change `'YOUR-CLIENT-ID'` in [`static/js/render.js`][5] and 
   [`tictactoe_api.py`][6] to the respective client ID(s) you have registered 
   in the [APIs Console][7].
3. Update the value of `application` in [`app.yaml`][8] from `your-app-id` 
   to the app ID you have registered in the App Engine admin console and would 
   like to use to host your instance of this sample.
4. Run the application, and ensure it's running by visiting your local server's
   admin console (by default [localhost:8080/_ah/admin][9].)
5. Test your Endpoints by visiting the Google APIs Explorer: 
  [localhost:8080/_ah/api/explorer][10]

[1]: https://developers.google.com/appengine
[2]: http://python.org/
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://developers.google.com/appengine/downloads
[5]: https://github.com/GoogleCloudPlatform/appengine-endpoints-tictactoe-python/blob/master/static/js/render.js
[6]: https://github.com/GoogleCloudPlatform/appengine-endpoints-tictactoe-python/blob/master/tictactoe_api.py
[7]: https://code.google.com/apis/console
[8]: https://github.com/GoogleCloudPlatform/appengine-endpoints-tictactoe-python/blob/master/app.yaml
[9]: http://localhost:8080/_ah/admin
[10]: http://localhost:8080/_ah/api/explorer
