# SimplyBlog
A very basic, minimal blogging template written in Flask

Demo: https://blog.maxbridgland.com

# Getting Started

### Installation

To start you need to have `Python 3` (written on and maintained in Python 3.6.8 so use this distro for the best results). Run:

```
pip3 install -r requirements.txt
```

This will get you setup with all the dependencies you will need.

Next head into the `app/__init__.py` file and modify the config to suit your needs. This is the config without any modifications when you pull the repo:

```
app.config.update({
    'website_name': 'Title on landing page',
    'website_desc': 'Subtitle below this title ^',
    'name': 'Your name/publishing name',
    'timezone': pytz.timezone('America/Chicago'), # ENTER YOUR TIMEZONE HERE
    'secret_key': 'random-key-here', # PUT A SECRET KEY TO UPLOAD WITH, MAKE IT RANDOM TO INCREASE SECURITY!
    'base_url': 'https://blog.myblog.com', # DOMAIN THE BLOG/API WILL BE RUNNING ON
    'web_title': 'My Blog' # TITLE FOR HTML IN THE TAB
})
```

Pretty self explainatory and I gave you some nice comments if you get confused.

**This is as bare minimum of a blog as it gets really lol**

### Running the Server

To run your new blog site simply run: `flask run` and you will see it is available on `http://localhost:5000/` head to this address and test everything out. (Your base_url should be set to `localhost:5000` when doing local development and testing).

### Posting To The Blog

To post to the blog make sure your app is running and then head to the `/panel` endpoint. You'll see a pretty little upload panel and a secret key input. You set this secret key in your config.

![preview](https://i.imgur.com/4zwLppK.png)

### Contributing

If you feel like there could be better changes or you'd like to write some tests go ahead! I have no real contribution guideline for this project as I doubt it will get used much anyways! Enjoy!
