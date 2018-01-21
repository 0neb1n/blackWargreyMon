#-*- coding: utf-8 -*-
#author : 0neb1n

from flask import Flask, request
from flask_restful import Resource, Api
from json import dump
from flask.ext.jsonpify import jsonify

import jenkins
import yaml

stream = open("config.yaml", "r")
conf = yaml.load(stream)

jenkins_url = conf['jenkins_url']
jenkins_username = conf['jenkins_username']
jenkins_token = conf['jenkins_token']

server = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_token)
app = Flask(__name__)
api = Api(app)

class Builds(Resource):
    def post(self):
        #if 1 < len(params = request.form['text'].split('')):
        #    return 404
        job_name = request.form['text']
        server.build_job(job_name, token=jenkins_token)
        last_build_number = server.get_job_info(job_name)['nextBuildNumber']
        build_url = jenkins_url + "/job/" + job_name + "/" + str(last_build_number)

        return "build job started - " + build_url

api.add_resource(Builds,'/builds')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
