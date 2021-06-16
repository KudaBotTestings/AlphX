const yaml = require('js-yaml');
const fs = require('fs');
var path = require('path');
var util = require('util');

var configPath = './configs/config.yaml';

function changePath(path) {
    configPath = path;
}

function load() {
    try {
        var filePath = path.join(__dirname,configPath);
        var fileContents = fs.readFileSync(filePath,'utf-8');
        var yamlData = yaml.load(fileContents);
        return yamlData;
    } catch (err) {
        console.log(err.stack || String(err));
    }
}

exports.filesystem = fs;
exports.yaml = yaml;
exports.systemPath = path;
exports.util = util;
exports.configPath = configPath;
exports.load = load;
exports.changePath = changePath;