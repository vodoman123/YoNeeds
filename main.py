#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import urllib2
import jinja2
import os

from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

api_token = "c1931e1c-a127-6821-af9e-4c89cb79e7d9"

all_access_url = "http://api.justyo.co/yoall/"
single_access_url = "https://api.justyo.co/yo/"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(main_template.render())

class YoOauth(webapp2.RequestHandler):
    def get(self):
        yo_name = self.request.get('yo-name')
        fctn = YoFunc()
        yo_user = fctn.yo_one(yo_name)
        yoauth_template = JINJA_ENVIRONMENT.get_template('templates/yoauth.html')
        self.response.write(yoauth_template.render())

class YoFunc:
    def yo_all(self):
    	data = {'api_token': api_token}
        data = urllib.urlencode(data)
    	request_object = urllib2.Request(all_access_url, data)
    	response = urllib2.urlopen(request_object)

    def yo_one(self, userName):
    	data = {'api_token': api_token, 'username': userName}
        data = urllib.urlencode(data)
    	request_object = urllib2.Request(single_access_url, data)
    	response = urllib2.urlopen(request_object)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/yoauth', YoOauth)
], debug=True)
